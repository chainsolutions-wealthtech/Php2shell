"""Offline-first, authorization-aware PHP inventory and advisory matching."""
from dataclasses import dataclass
from enum import Enum
import json
import re

class Scope(str, Enum):
    PUBLIC = 'public_metadata'
    OWNED = 'owned_source'

@dataclass(frozen=True)
class Target:
    hostname: str
    scope: Scope
    evidence: str = ''

    def __post_init__(self):
        host = self.hostname.strip().lower()
        # Validate each DNS label independently, not merely the whole name.
        # Total length <= 253, each ASCII label 1..63 chars, no leading or
        # trailing hyphen. This intentionally rejects URLs and IDN Unicode:
        # callers must first convert authorized IDNs to ASCII/Punycode.
        if (not host or len(host) > 253 or
                any(not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', label)
                    for label in host.split('.'))):
            raise ValueError('Invalid hostname')
        object.__setattr__(self, 'hostname', host)
        if self.scope == Scope.OWNED and not self.evidence.strip():
            raise ValueError('Owned-source scope requires authorization evidence')

# Configuration examples, not a validated live vulnerability feed.
ADVISORIES = {
    'CVE-2026-109618': {'8.3': '8.3.36', '8.4': '8.4.27', '8.5': '8.5.12', '8.2': '8.2.35'},
    'CVE-2026-109619': {'8.3': '8.3.36', '8.4': '8.4.27', '8.5': '8.5.12', '8.2': '8.2.35'},
}

def parse_version(version):
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Expected numeric PHP version X.Y.Z')
    return tuple(map(int, version.split('.')))

def evaluate(version):
    actual = parse_version(version)
    branch = '.'.join(version.split('.')[:2])
    result = []
    for cve, fixed in ADVISORIES.items():
        target = fixed.get(branch)
        status = ('review_vendor_support' if target is None else
                  'below_reference_fix' if actual < parse_version(target) else
                  'at_or_above_reference_fix')
        result.append({'cve': cve, 'status': status, 'reference_fix': target,
                       'note': 'Version comparison only; verify vendor backports and runtime configuration.'})
    return result

def inventory(targets):
    """Classify declarations without elevating unverified P2 source access.

    A nonempty user-supplied evidence reference is NOT an authenticated
    mandate, ownership proof, project claim, or resource authorization.
    Only a separate governed verifier may grant source access. This offline
    inventory has no such verifier and must therefore always fail closed.
    """
    return [{'hostname': t.hostname, 'scope': t.scope.value,
             'mandate_reference_supplied': bool(t.evidence),
             'authorization_verified': False,
             'source_access_allowed': False} for t in targets]

def load_targets(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError('Expected a JSON list')
    return [Target(item['hostname'], Scope(item['scope']), item.get('evidence', '')) for item in data]
