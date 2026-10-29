"""Short, honest anonymous summary of supplied public HTTP metadata.

A *pure* formatter/validator: this does not send a request, authenticate a
user, establish collector provenance, determine CVE exploitability, or save
any report. A production public scanner must separately implement approved
admission, DNS/SSRF guards, redirects, quotas and trusted evidence collection.
"""
from .url_intake import preview_url_scope


_ALLOWED_HEADERS = frozenset({
    "content-type",
    "strict-transport-security",
    "content-security-policy",
    "x-content-type-options",
    "referrer-policy",
    "permissions-policy",
})
_REQUIRED = frozenset({
    "schema_version", "evidence_type", "http_status",
    "response_headers_present",
})
_RECOMMENDED = (
    ("strict-transport-security",
     "La présence de l'en-tête HSTS n'est pas indiquée dans les éléments fournis."),
    ("content-security-policy",
     "La présence d'une politique CSP n'est pas indiquée dans les éléments fournis."),
    ("x-content-type-options",
     "La présence de X-Content-Type-Options n'est pas indiquée dans les éléments fournis."),
)


def _validate_evidence(evidence):
    if not isinstance(evidence, dict) or set(evidence) != _REQUIRED:
        raise ValueError("Invalid unverified public evidence schema")
    if (evidence["schema_version"] != "0.2"
            or evidence["evidence_type"]
            != "UNVERIFIED_SUPPLIED_PUBLIC_RESPONSE"):
        raise ValueError("Unsupported public evidence")
    status = evidence["http_status"]
    if type(status) is not int or not 100 <= status <= 599:
        raise ValueError("Invalid declared HTTP status")
    headers = evidence["response_headers_present"]
    if (not isinstance(headers, list) or len(headers) > len(_ALLOWED_HEADERS)
            or len(headers) != len(set(str(x) for x in headers))
            or any(not isinstance(h, str) or h not in _ALLOWED_HEADERS
                   for h in headers)):
        raise ValueError("Invalid public header-name indicators")
    return status, set(headers)


def build_guest_public_summary(url, public_response_evidence=None):
    """Return ≤3 short indicators, without remote inspection or storage.

    A supplied snapshot is NOT proof that it came from the URL, even if
    the caller says it did. This function deliberately cannot return a
    site security rating, detailed report, or authenticated ownership.
    """
    preview = preview_url_scope(url, scope="public_metadata")
    result = {
        "schema_version": "0.2",
        "summary_type": "ANONYMOUS_SHORT_PREVIEW",
        "hostname": preview["hostname"],
        "status": "NOT_ANALYZED",
        "headline": "Adresse acceptée. Aucune analyse réelle du site n'a été effectuée.",
        "observations": [],
        "site_contacted": False,
        "network_requests_made": False,
        "audit_performed": False,
        "vulnerability_confirmed": False,
        "site_ownership_verified": False,
        "detailed_report_available": False,
        "can_read_detailed_report": False,
        "report_stored": False,
        "account_required_for_report_storage": True,
        "can_read_private_source": False,
        "can_patch": False,
        "can_deploy": False,
        "next_action": "SIGN_IN_FOR_PERSISTENT_DETAILED_REPORT",
        "limitations": (
            "Aucun site contacté. Une URL seule ne constitue pas un audit. "
            "Une analyse publique réelle nécessite une collecte admise et "
            "contrôlée ; un rapport privé exige une connexion et des droits."
        ),
    }
    if public_response_evidence is None:
        return result

    status, present = _validate_evidence(public_response_evidence)
    observations = [{
        "label": "Statut HTTP déclaré",
        "message": "Un échantillon non vérifié indique le statut HTTP "
                   + str(status) + ".",
        "evidence_verified": False,
    }]
    for name, missing_notice in _RECOMMENDED:
        if len(observations) >= 3:
            break
        if name not in present:
            observations.append({
                "label": "Information de sécurité à confirmer",
                "message": missing_notice,
                "evidence_verified": False,
            })
    result["status"] = "UNVERIFIED_SUPPLIED_EVIDENCE"
    result["headline"] = (
        "Aperçu limité fondé sur des informations fournies, non vérifiées "
        "sur le site. Il ne s'agit pas d'un audit."
    )
    result["observations"] = observations
    return result
