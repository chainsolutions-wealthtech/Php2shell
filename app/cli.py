import argparse
import json
from .core import evaluate, inventory, load_targets
from .static_analysis import scan_project
from .campaign_import import import_targets
from .reporting import export_findings_csv
from .security_advisories import list_verified_advisories, review_declared_php_version
from .catalog_audit import audit_catalog_snapshot
from .catalog_update import propose_catalog_update
from .advisory_fetch import fetch_curated_php_advisory

def main():
    parser = argparse.ArgumentParser(description='PHP2SHELL offline defensive prototype')
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check-version')
    check.add_argument('--php', required=True)
    inv = sub.add_parser('inventory')
    inv.add_argument('--file', required=True)
    scan = sub.add_parser('scan-local', help='Read-only PHP and Composer source inventory')
    scan.add_argument('--path', required=True, help='Authorized local project directory')
    scan.add_argument('--format', choices=('json', 'csv'), default='json',
                      help='Result format; CSV is a findings-only summary')
    camp = sub.add_parser('import-targets', help='Preview an offline JSON, CSV or TXT campaign')
    camp.add_argument('--file', required=True, help='Local file only; no network requests')
    sub.add_parser('advisories', help='List dated official PHP advisory references from local snapshot')
    audit = sub.add_parser('audit-catalog', help='Offline snapshot age and provenance, NOT a live feed')
    audit.add_argument('--as-of', required=True, help='Explicit UTC calendar date YYYY-MM-DD')
    sourced = sub.add_parser('review-version', help='Sourced version comparison, NOT asset diagnosis')
    sourced.add_argument('--php', required=True, help='User-declared PHP version only')
    proposal = sub.add_parser('propose-catalog-update',
                              help='Review a local candidate advisory JSON without applying it')
    proposal.add_argument('--candidate', required=True, help='Local JSON candidate, never fetched remotely')
    proposal.add_argument('--as-of', required=True, help='Explicit UTC date YYYY-MM-DD')
    fetch = sub.add_parser('fetch-official-advisory',
                           help='Explicit bounded GitHub API lookup of a known GHSA (network)')
    fetch.add_argument('--ghsa', required=True, help='Must already be in curated catalog')
    fetch.add_argument('--as-of', required=True, help='Explicit UTC observation date YYYY-MM-DD')
    fetch.add_argument('--permit-official-network', required=True, action='store_true',
                       help='Explicit opt-in: contacts only api.github.com over HTTPS')
    args = parser.parse_args()
    if args.command == 'check-version':
        result = evaluate(args.php)
    elif args.command == 'inventory':
        result = inventory(load_targets(args.file))
    elif args.command == 'advisories':
        result = list_verified_advisories()
    elif args.command == 'review-version':
        result = review_declared_php_version(args.php)
    elif args.command == 'audit-catalog':
        result = audit_catalog_snapshot(args.as_of)
    elif args.command == 'propose-catalog-update':
        result = propose_catalog_update(args.candidate, args.as_of)
    elif args.command == 'fetch-official-advisory':
        result = fetch_curated_php_advisory(args.ghsa, args.as_of)
    elif args.command == 'scan-local':
        result = scan_project(args.path)
    else:
        result = import_targets(args.file)
    if args.command == 'scan-local' and args.format == 'csv':
        print(export_findings_csv(result), end='')
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
