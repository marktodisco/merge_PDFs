import argparse
import os
from glob import glob
from typing import Iterable, List, Union


def parse_arguments(args: List[str]) -> argparse.Namespace:
    """
    Extract command line arguments.

    Parameters
    ----------
    args : list
        Program arguments. See Notes section.

    Returns
    -------
    argparse.Namespace
        Returns the parsed arguments that were passed into the function.
        Arguments can be accessed using dot notation.

    Notes
    -----
    The only valid arguments are as follows.

    -f : Name(s) of file(s) to be combined.
    -o : Name of output file.
    -d : Name of input directory. Selects all PDfS in the specifed directory.
    """
    parser = argparse.ArgumentParser(prog='pdfmerge',
                                     description="Merge pdf files.")

    parser.add_argument(
        '-f', '--files', nargs='*', help='File names.', default=None)
    parser.add_argument(
        '-o', '--output-name', help='Ouput file name.', default=None)
    parser.add_argument(
        '-d', '--input-dir', help='Input directory.', default=None)
    parsed_args = parser.parse_args()

    return parsed_args


def validate_directory(dir_path: Union[str, os.PathLike]) -> List[str]:
    """
    Get all PDF file names in a directory.

    Parameters
    ----------
    dir_path : str
        Path to the directory that will be searched.

    Returns
    -------
    List[str]
        List of paths to each PDF file in `dir_path`.
    """
    wildcard = os.path.join(dir_path, '*.pdf')
    all_pdfs = glob(wildcard)
    return all_pdfs


def print_files(files: List[str]):
    """
    Display file name and assign them an index.

    Parameters
    ----------
    files : List[str]
        List of files to display via CLI.
    """
    msg_template = '[{}] {}'
    parent = os.path.dirname(files[0])
    print(f'Parent Directory: {parent}')
    for i, f in enumerate(files):
        trimmed_file = f.replace(parent, '')
        print(msg_template.format(i+1, trimmed_file))
