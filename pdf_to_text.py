import PyPDF2


def pdfToText(file_path):
    #     # We use 'rb' instead of just 'r' when opening a file because PDF files, and some other file formats, are binary files
    f = open(file_path, "rb")
    text = ""
    reader = PyPDF2.PdfFileReader(f)

    for noOfPage in range(reader.numPages):
        page = reader.getPage(noOfPage)
        text += page.extract_text()
    return text
