import unittest
from pathlib import Path

from pdfmerge.utils import validate_output_name_and_handle_error


class TestOutputName(unittest.TestCase):

    def test_output_file_is_pdf(self):
        output_name = validate_output_name_and_handle_error('test.pdf')
        self.assertTrue(Path(output_name).suffix == '.pdf')

    def test_raise_error_if_not_pdf(self):
        with self.assertRaises(ValueError):
            _ = validate_output_name_and_handle_error('test.txt')

    def test_path_is_absolute(self):
        output_name = validate_output_name_and_handle_error('./test.pdf')
        self.assertTrue(Path(output_name).is_absolute())


if __name__ == '__main__':
    unittest.main()
