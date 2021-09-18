import unittest
from pathlib import Path
import shutil
import filecmp

from pdfmerge.pdf import merge


class TestMergeFiles(unittest.TestCase):

    def setUp(self) -> None:
        self.baseline_file = Path('./tests/baseline.pdf').resolve()

        self.output_dir: Path = Path('./tests/temp').resolve()
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.output_name = (self.output_dir / 'output.pdf').resolve()
        self.files = [
            str(Path(f'./tests/{i}.pdf').resolve())
            for i in range(1, 4)
        ]

    def tearDown(self) -> None:
        shutil.rmtree(self.output_dir)

    def test_merge_files(self):
        merge(self.files, output_name=self.output_name)

        [output_file] = list(self.output_dir.glob('*.pdf'))

        files_are_equal = filecmp.cmp(
            self.baseline_file, output_file, shallow=False
        )

        self.assertTrue(files_are_equal)


if __name__ == '__main__':
    unittest.main()
