import argparse
import json
from .core import evaluate, inventory, load_targets
from .static_analysis import scan_project
from .campaign_import import import_targets
from .reporting import export_findings_csv

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
    args = parser.parse_args()
    if args.command == 'check-version':
        result = evaluate(args.php)
    elif args.command == 'inventory':
        result = inventory(load_targets(args.file))
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
