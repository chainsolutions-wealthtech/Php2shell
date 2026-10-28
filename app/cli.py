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
from .runtime_evidence import review_declared_runtime_evidence
from .runtime_reporting import export_runtime_review_csv
from .audit_dossier import build_audit_dossier, render_audit_dossier_markdown
from .url_intake import preview_url_scope
from .patch_preview import propose_local_ini_patch
from .patch_rehearsal import rehearse_local_ini_patch
from .patch_review_packet import build_patch_review_packet
from .patch_packet_verifier import load_and_verify_local_review_packet
from .campaign_plan import plan_offline_campaign
from .report_html import render_dossier_html

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
    runtime = sub.add_parser('review-runtime-evidence',
                             help='Inspect a local declared PHP/SAPI snapshot, NOT a verified runtime')
    runtime.add_argument('--file', required=True, help='Local JSON only; no network or PHP execution')
    runtime.add_argument('--as-of', required=True, help='Explicit UTC calendar date YYYY-MM-DD')
    runtime.add_argument('--format', choices=('json', 'csv'), default='json',
                         help='CSV is a limited unverified comparison summary')
    dossier = sub.add_parser('audit-dossier',
                             help='Assemble offline review-only audit dossier, no code/secret export')
    dossier.add_argument('--path', required=True, help='Authorized local PHP project')
    dossier.add_argument('--as-of', required=True, help='UTC calendar date YYYY-MM-DD')
    dossier.add_argument('--runtime-file', help='Optional unverified local PHP runtime JSON')
    dossier.add_argument('--format', choices=('json', 'markdown', 'html'), default='json')
    url_preview = sub.add_parser('preview-url',
                                 help='Offline URL scope preview, NOT an audit or mandate')
    url_preview.add_argument('--url', required=True, help='Public HTTPS site URL')
    url_preview.add_argument('--scope', choices=('public_metadata','owned_source'),
                             default='public_metadata')
    url_preview.add_argument('--mandate-ref', help='Unverified operator reference, not output')
    url_preview.add_argument('--max-pages', type=int, default=20)
    url_preview.add_argument('--requests-per-minute', type=int, default=6)
    campaign = sub.add_parser('plan-campaign',
                              help='Offline partitions only; no worker, crawl or permission')
    campaign.add_argument('--file', required=True, help='Existing JSON/CSV/TXT inventory')
    campaign.add_argument('--tag', default='local-preview')
    campaign.add_argument('--shards', type=int, default=4)
    campaign.add_argument('--pages-per-target', type=int, default=20)
    campaign.add_argument('--requests-per-minute', type=int, default=6)
    patch_proposal = sub.add_parser('propose-config-patch',
                                    help='Offline php.ini display_errors diff; NEVER applied')
    patch_proposal.add_argument('--path', required=True, help='Authorized local PHP project directory')
    patch_proposal.add_argument('--as-of', required=True, help='UTC calendar date YYYY-MM-DD')
    patch_proposal.add_argument('--evidence-id', required=True, help='One local dossier P2S-EV indicator')
    rehearsal = sub.add_parser('rehearse-config-patch',
                               help='In-memory single php.ini replacement with byte-exact rollback; NEVER applied')
    rehearsal.add_argument('--path', required=True, help='Authorized local project directory')
    rehearsal.add_argument('--as-of', required=True, help='UTC calendar date YYYY-MM-DD')
    rehearsal.add_argument('--evidence-id', required=True, help='Current local PHP config evidence ID')
    review_packet = sub.add_parser('prepare-patch-review',
                                   help='Non-executing PHPPATCH evidence lineage + rollback review packet')
    review_packet.add_argument('--path', required=True, help='Authorized local project only')
    review_packet.add_argument('--as-of', required=True, help='UTC calendar date YYYY-MM-DD')
    review_packet.add_argument('--evidence-id', required=True, help='Current local evidence ID')
    verify_packet = sub.add_parser('verify-patch-review',
                                   help='Revalidate a local PHPPATCH packet; NOT an approval')
    verify_packet.add_argument('--packet-file', required=True,
                               help='Local JSON packet file, never uploaded')
    verify_packet.add_argument('--path', required=True,
                               help='Authorized local project directory')
    verify_packet.add_argument('--as-of', required=True,
                               help='UTC date used to create the packet')
    verify_packet.add_argument('--evidence-id', required=True,
                               help='Current local PHP configuration evidence ID')
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
    elif args.command == 'review-runtime-evidence':
        result = review_declared_runtime_evidence(args.file, args.as_of)
    elif args.command == 'audit-dossier':
        result = build_audit_dossier(args.path, args.as_of, args.runtime_file)
    elif args.command == 'preview-url':
        result = preview_url_scope(args.url, args.scope, args.mandate_ref,
                                   args.max_pages, args.requests_per_minute)
    elif args.command == 'plan-campaign':
        result = plan_offline_campaign(
            args.file, campaign_tag=args.tag, shards=args.shards,
            pages_per_target=args.pages_per_target,
            requests_per_minute=args.requests_per_minute,
        )
    elif args.command == 'propose-config-patch':
        result = propose_local_ini_patch(args.path, args.as_of, args.evidence_id)
    elif args.command == 'rehearse-config-patch':
        result = rehearse_local_ini_patch(args.path, args.as_of, args.evidence_id)
    elif args.command == 'prepare-patch-review':
        result = build_patch_review_packet(args.path, args.as_of, args.evidence_id)
    elif args.command == 'verify-patch-review':
        try:
            result = load_and_verify_local_review_packet(
                args.packet_file, args.path, args.as_of, args.evidence_id,
            )
        except (ValueError, OSError):
            parser.error('Local PHPPATCH review packet rejected')
    elif args.command == 'scan-local':
        result = scan_project(args.path)
    else:
        result = import_targets(args.file)
    if args.command == 'audit-dossier' and args.format == 'html':
        print(render_dossier_html(result), end='')
    elif args.command == 'audit-dossier' and args.format == 'markdown':
        print(render_audit_dossier_markdown(result), end='')
    elif args.command == 'review-runtime-evidence' and args.format == 'csv':
        print(export_runtime_review_csv(result), end='')
    elif args.command == 'scan-local' and args.format == 'csv':
        print(export_findings_csv(result), end='')
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
