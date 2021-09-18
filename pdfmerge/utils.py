import argparse
import os
from pathlib import Path
from typing import List, Union


def parse_arguments(
    args: Union[List[str], argparse.Namespace]
) -> argparse.Namespace:
    if isinstance(args, argparse.Namespace):
        return args
    parser = argparse.ArgumentParser(
        prog='pdfmerge', description="Merge pdf files."
    )
    parser.add_argument('-f', '--files', nargs='*', help='File names.')
    parser.add_argument('-o', '--output-name', help='Ouput file name.')
    parser.add_argument('-d', '--input-dir', help='Input directory.')
    return parser.parse_args(args)


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
    # wildcard = os.path.join(dir_path, '*.pdf')
    # all_pdfs = glob(wildcard)
    # return all_pdfs
    return [str(path) for path in Path(dir_path).glob('*.pdf')]


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
