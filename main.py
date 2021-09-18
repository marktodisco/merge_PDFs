import argparse
import sys
from typing import Iterable

from pdfmerge import utils
from pdfmerge.pdf import merge


def main(args: argparse.Namespace = None) -> None:
    parsed_args = utils.parse_arguments(args or sys.argv[1:])
    files = get_files(parsed_args)
    if files is None:
        print('\nCANCELLED\n')
        return
    merge(files, parsed_args.output_name)


def get_files(args: argparse.Namespace) -> Iterable[str]:
    if args.files is not None:
        files = args.files
    elif args.input_dir is not None:
        files = utils.get_pdf_files(args.input_dir)
    else:
        raise ValueError(f'Invalid files: {args.files}')
    return files
