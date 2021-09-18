from pathlib import Path
from typing import Iterable, List

import PyPDF2


def merge(files: Iterable[str], output_name: str = None) -> None:
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

    save_path = 'merged.pdf' if output_name is None else output_name
    save_path = str(Path(save_path).resolve())

    merger = PDFMerger(files, save_path)
    merger.read()
    merger.write()


class PDFMerger:
    pdf: List[PyPDF2.PdfFileReader] = []

    def __init__(self, files: Iterable[str], output: str):
        if not isinstance(files, Iterable):
            raise Exception('`files` must be a str or list')

        self.file_path = files
        self._num_files = 0
        self.writer = PyPDF2.PdfFileWriter()
        self.output = output

    def read(self):
        self.__read_pdf()
        self.__add_pages_to_writer()

    def write(self):
        self.__write_pages_to_file()

    def __read_pdf(self):
        for file in self.file_path:
            self.pdf.append(PyPDF2.PdfFileReader(file, strict=False))
            self._num_files += 1

    def __add_pages_to_writer(self):
        for pdf in self.pdf:
            num_pages = pdf.getNumPages()
            for i in range(num_pages):
                page = pdf.getPage(i)
                self.writer.addPage(page)

    def __write_pages_to_file(self):
        with open(self.output, 'wb') as output:
            self.writer.write(output)
        print(f'Merged file was written to {self.output}\n')
