import argparse
import sys
from typing import Iterable

from pdfmerge import utils
from pdfmerge.pdf import merge


def main(args: argparse.Namespace = None) -> None:
    parsed_args = utils.parse_arguments(args or sys.argv[1:])
    files = get_files(parsed_args)
    if files is not None:
        merge(files, parsed_args.output_name)
    else:
        print('\nCANCELLED\n')


def get_files(parsed_args: argparse.Namespace) -> Iterable[str]:
    # Selection of file can come directly from the `args` or can be selected
    # using the GUI. These actions should be assigned to a separate part of
    # the program.
    if parsed_args.files is not None:
        # OrderedFileSelectionStrategy
        files = parsed_args.files
    elif parsed_args.input_dir is not None:
        # DirectoryFileSelectionStrategy
        files = utils.validate_directory(parsed_args.input_dir)
    else:
        raise ValueError(f'Invalid files: {parsed_args.files}')
    return files
