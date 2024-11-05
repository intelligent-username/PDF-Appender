from PyPDF2 import PdfReader

def get_pdf_paths():
    """Prompt user for PDF file paths and return them as a list."""
    num_files = int(input("Enter the number of PDF files to merge: "))
    file_paths = []
    for i in range(num_files):
        path = input(f"Enter path for file {i+1}: ")
        file_paths.append(path)
    return file_paths

def load_pdfs(file_paths):
    """Load each PDF as a PdfReader object."""
    readers = []
    for path in file_paths:
        readers.append(PdfReader(path))
    return readers
