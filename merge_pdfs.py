from PDFMerger import PDFMerger
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


def run():
    # Get file names from 'pdfs' dir
    Tk().withdraw()
    files = askopenfilenames(initialdir='./', title='Chose files to merge', filetypes=(('PDF', '*.pdf'), ('PDF files', '*.pdf')))

    # Create merger object
    if files == '':
        print('Program stopped by user.')
    else:
        save_path = os.path.join(r'C:\\Users\\markt\\OneDrive\\Desktop', 'merged.pdf')
        # print(save_path)
        merger = PDFMerger(files, save_path)


if __name__ == '__main__':
    run()