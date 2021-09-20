import argparse
import sys

from pdfmerge.pdf import merge
from pdfmerge.utils import get_files, parse_arguments


def main(args: argparse.Namespace = None) -> None:
    parsed_args = parse_arguments(args or sys.argv[1:])
    files = get_files(parsed_args)

    if files is None:
        print('\nCANCELLED\n')
        return

    merge(files, parsed_args.output_name)
