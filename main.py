import argparse
import sys

from pdfmerge.pdf import merge
from pdfmerge.utils import (
    get_files,
    parse_arguments,
    validate_paths_and_handle_error,
)


def main(args: argparse.Namespace = None) -> None:
    parsed_args = parse_arguments(args or sys.argv[1:])
    files = get_files(parsed_args)
    files = validate_paths_and_handle_error(files)

    if files is None:
        print('\nCANCELLED\n')
        return

    merge(files, parsed_args.output_name)
