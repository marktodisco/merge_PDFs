import unittest

from pdfmerge.utils import parse_arguments


class DynamicTestCase(unittest.TestCase):

    num_files = 3
    files = [f'{i}.pdf' for i in range(1, num_files + 1)]
    output_name = 'output.pdf'

    def test_files_are_parased_correctly(self) -> None:
        for i in range(1, self.num_files + 1):
            with self.subTest(i=i):
                parsed = parse_arguments(['-f', *self.files[:i]])
                self.assertEqual(parsed.files, [*self.files[:i]])

    def test_custom_output_is_parased_correctly(self) -> None:
        for i in range(1, self.num_files + 1):
            with self.subTest(i=i):
                parsed = parse_arguments(
                    ['-f', *self.files, '-o', self.output_name]
                )
                self.assertEqual(parsed.output_name, self.output_name)


if __name__ == '__main__':
    unittest.main()
