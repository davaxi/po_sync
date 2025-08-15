import argparse
from .core import PoSync

def main():
    parser = argparse.ArgumentParser(
        description="PoSync is an open-source CLI tool that automatically syncs .po file msgid keys with applied corrections and updates the source code at the exact lines referenced in the .po, eliminating tedious manual replacements.",
        add_help=True
    )
    parser.add_argument('file_path', help='Path to .po file with corrections')
    parser.add_argument('-d', '--folder-path', help='Path to base project\'s folder', nargs='?', default='.')
    parser.add_argument('-t', '--dry-run', help='Dry run', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
    parser.add_argument('-y', '--yes', help='Do not ask for confirmation', action='store_true')

    args = parser.parse_args()

    engine = PoSync(args.file_path, args.folder_path, args.dry_run, args.verbose, args.yes)
    engine.run()

if __name__ == "__main__":
    main()