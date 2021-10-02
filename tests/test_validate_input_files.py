import unittest
from pathlib import Path
from typing import Sequence

from pdfmerge.utils import validate_files_and_handle_error


class TestValidateFiles(unittest.TestCase):

    def test_files_have_pdf_extension(self) -> None:
        files = [f'{i}.pdf' for i in range(3)]
        validate_files_and_handle_error(files)

    def test_raises_value_error_for_non_pdf_files(self) -> None:
        files = [f'{i}.txt' for i in range(3)]
        with self.assertRaises(ValueError):
            validate_files_and_handle_error(files)

    def test_raises_value_error_for_non_pdf_files_with_one_invalid(
        self
    ) -> None:
        files = [f'{i}.pdf' for i in range(3)] + ['3.txt']
        with self.assertRaises(ValueError):
            validate_files_and_handle_error(files)

    def test_returns_string_paths(self) -> None:
        files: Sequence[str] = [f'{i}.pdf' for i in range(3)]
        files = validate_files_and_handle_error(files)
        self.assertTrue(all(map(lambda file: isinstance(file, str), files)))

    def test_files_are_absolute(self):
        files: Sequence[str] = [f'{i}.pdf' for i in range(3)]
        files = validate_files_and_handle_error(files)
        self.assertTrue(all(map(lambda file: Path(file).is_absolute(), files)))


if __name__ == '__main__':
    unittest.main()
