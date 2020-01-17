from PDFMerger import PDFMerger
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


# Get file names from 'pdfs' dir
Tk().withdraw()
files = askopenfilenames(initialdir='./', title='Chose files to merge', filetypes=(('PDF', '*.pdf'), ('PDF files', '*.pdf')))

# Create merger object
if files == '':
    print('Program stopped by user.')
else:
    output = os.path.join(os.getcwd(), 'merged.pdf')
    merger = PDFMerger(files, output)
