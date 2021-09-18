import argparse
import os
from pathlib import Path
from typing import Iterable, List, Sequence, Union


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


def get_pdf_files(dir_path: Union[str, os.PathLike]) -> Iterable[str]:
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
    return (str(path) for path in Path(dir_path).glob('*.pdf'))
