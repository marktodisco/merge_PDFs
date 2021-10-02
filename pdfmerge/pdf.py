from typing import Sequence

import PyPDF2

from pdfmerge.utils import (
    validate_files_and_handle_error,
    validate_output_name_and_handle_error
)


def merge(files: Sequence[str], output_name: str = None) -> None:
    """
    Combine separate PDF files into a single document.

    Parameters
    ----------
    files : List[str]
        List of file paths to merge.
    output_name : str, optional
        Path (including file name) to where the merged file will be saved.
        Default is None.
    """
    if files == '':
        print('Program stopped by user.')
        return

    files = validate_files_and_handle_error(files)
    output_name = validate_output_name_and_handle_error(
        'merged.pdf' if output_name is None else output_name
    )

    merger = PyPDF2.PdfFileMerger(strict=False)
    for file in files:
        merger.append(file)
    merger.write(output_name)
