# CLI Setup Using Anaconda/Miniconda

The following command create an Anaconda environment and installs the `pdfmerge` tool.
```shell
conda env create -f conda.yaml
```

The following command activates the virtual environment.
```shell
conda activate pdfmerge-dev
```

# Basic Help

```shell
pdfmerge -h
```
```
usage: pdfmerge [-h] [-f [FILES [FILES ...]]] [-o OUTPUT_NAME] [-d INPUT_DIR]

Merge pdf files.

optional arguments:
  -h, --help            show this help message and exit
  -f [FILES [FILES ...]], --files [FILES [FILES ...]]
                        File names.
  -o OUTPUT_NAME, --output-name OUTPUT_NAME
                        Output file name.
  -d INPUT_DIR, --input-dir INPUT_DIR
                        Input directory.
```

# Usage with File Paths

The following command merges `file1.pdf` and `file2.pdf` into a single PDF named `merged.pdf`.
```shell
pdfmerge -f file1.pdf file2.pdf -o merged.pdf
```

# Usage with Directories

The following command merges all the PDF files in the `my_pdf_files` folder into a single PDF named `merged.pdf`.
```shell
pdfmerge -d my_pdf_files -o merged.pdf
```
