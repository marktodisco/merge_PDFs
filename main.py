import argparse
import os
import sys

from typing import List

from pdfmerge.pdf import PDFMerger
from pdfmerge import utils


def main(args: argparse.Namespace = None) -> None:
    parsed_args = utils.parse_arguments(args or sys.argv[1:])

    # Selection of file can come directly from the `args` or can be selected
    # using the GUI. These actions should be assigned to a separate part of
    # the program.
    sort = True
    if parsed_args.files is not None:
        # OrderedFileSelectionStrategy
        files = parsed_args.files
        sort = False
    elif parsed_args.input_dir is not None:
        # DirectoryFileSelectionStrategy
        files = utils.validate_directory(parsed_args.input_dir)
    else:
        # This is NOT a PDFMergerStrategy. This is just a way of selecting
        # files, and should be separated from main().
        files = utils.get_files(os.getcwd())

    if files is not None:
        merge(files, parsed_args.output_name, sort)
    else:
        print('\nCANCELLED\n')
