def ask_blank_page_count():
    add_blanks = input("Would you like to add blank pages between files? (yes/no): ").strip().lower()
    if add_blanks == "yes":
        return int(input("How many blank pages to add between files? "))
    return 0

def get_output_filename():
    return input("Enter the name for the output PDF file (e.g., output.pdf): ")
