# main.py
from file_handler import get_pdf_paths, load_pdfs
from pdf_operations import merge_pdfs
from interface import ask_blank_page_count, get_output_filename

def main():
    # Collect file paths
    file_paths = get_pdf_paths()
    
    # Load PDFs
    readers = load_pdfs(file_paths)
    
    # User specifies blank pages
    num_blank_pages = ask_blank_page_count()
    
    # Merge PDFs
    writer = merge_pdfs(readers, num_blank_pages)
    
    # Save the output file
    output_file = get_output_filename()
    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)
    print(f"PDFs merged successfully into {output_file}")

if __name__ == "__main__":
    main()
