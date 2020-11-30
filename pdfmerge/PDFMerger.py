import PyPDF2


class PDFMerger:

    def __init__(self, files, output):

        # Validate arguments
        if isinstance(files, tuple):
            files = list(files)
        elif (not isinstance(files, str)) and (not isinstance(files, list)):
            raise Exception('\'files\' must be a \'str\' or \'list\'')

        self.file_path = files
        self.fid = None
        self._num_files = 0
        self.pdf = None
        self.writer = PyPDF2.PdfFileWriter()
        self.output = output
        
    def read(self):
        self.__read_pdf()
        self.__add_pages_to_writer()
        
    def write(self):
        self.__write_pages_to_file()

    def __read_pdf(self):
        if isinstance(self.file_path, str):  # If one path is passed in
            self.fid = open(self.file_path, 'rb')
            self.pdf = PyPDF2.PdfFileReader(self.fid)
            self._num_files = 1

        elif isinstance(self.file_path, list):  # If more than 1 path is passed in
            self.fid = []
            self.pdf = []
            for file in self.file_path:
                fid = open(file, 'rb')
                self.fid.append(fid)
                self.pdf.append(PyPDF2.PdfFileReader(fid))
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

    def __del__(self):
        if self._num_files == 1 and not isinstance(self.fid, list):
            self.fid.close()
        else:
            for fid in self.fid:
                fid.close()
