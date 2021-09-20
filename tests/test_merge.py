import unittest
from pathlib import Path
import shutil
import filecmp


from pdfmerge.pdf import merge


class TestMergeFiles(unittest.TestCase):

    def setUp(self) -> None:
        TESTS_PATH = Path('./tests').resolve()

        self.baseline_file = TESTS_PATH / 'baseline.pdf'

        self.output_dir: Path = TESTS_PATH / 'temp'
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.output_name = self.output_dir / 'output.pdf'
        self.files = [str(TESTS_PATH / f'{i}.pdf') for i in range(1, 4)]

    def tearDown(self) -> None:
        shutil.rmtree(self.output_dir)

    def test_merge_files(self) -> None:
        merge(self.files, output_name=str(self.output_name))

        [output_file] = list(self.output_dir.glob('*.pdf'))

        files_are_equal = filecmp.cmp(
            self.baseline_file, output_file, shallow=False
        )

        self.assertTrue(files_are_equal)


if __name__ == '__main__':
    unittest.main()
