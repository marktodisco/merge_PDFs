from argparse import Namespace
from pathlib import Path
import unittest

from pdfmerge.utils import get_files


class TestGetFiles(unittest.TestCase):

    def test_files_pass_through_if_already_a_list(self) -> None:
        files = ['a', 'b', 'c']
        args = Namespace(files=files)
        self.assertSequenceEqual(get_files(args), files)

    def test_files_are_collected_from_directory(self) -> None:
        input_dir = './src/tests'
        args = Namespace(files=None, input_dir=input_dir)

        actual_files = [str(Path(f)) for f in get_files(args)]
        actual_files.remove(str(Path(f'{input_dir}/baseline.pdf')))

        expected_files = [
            str(Path(f'{input_dir}/{i}.pdf')) for i in range(1, 4)
        ]

        self.assertSequenceEqual(actual_files, expected_files)

    def test_raises_error_for_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            args = Namespace(files=None, input_dir=None)
            _ = get_files(args)


if __name__ == '__main__':
    unittest.main()
