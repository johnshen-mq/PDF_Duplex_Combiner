import os
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(odd_pages_file: str, even_pages_file: str, output_file: str) -> None:
    """Merge odd and even pages into a single PDF."""
    # Read the PDF files
    odd_reader = PdfReader(odd_pages_file)
    even_reader = PdfReader(even_pages_file)

    # Reverse the pages of the even pages PDF
    even_pages = list(even_reader.pages)
    even_pages.reverse()

    # Merge the pages
    merged_writer = PdfWriter()

    for i in range(len(odd_reader.pages)):
        merged_writer.add_page(odd_reader.pages[i])
        if i < len(even_pages):
            merged_writer.add_page(even_pages[i])

    # Write the merged PDF to the output file
    with open(output_file, "wb") as out_file:
        merged_writer.write(out_file)


def get_pdf_file(prompt):
    while True:
        file_path = input(prompt)
        if os.path.isfile(file_path) and file_path.lower().endswith('.pdf'):
            return file_path
        else:
            print("Invalid file. Please provide a valid PDF file.")


def main():
    print("PDF Page Merger")

    # Get the odd pages PDF file from the user
    odd_pages_file = get_pdf_file("Please provide the path to the PDF file with odd-numbered pages: ")

    # Get the even pages PDF file from the user
    even_pages_file = get_pdf_file(
        "Please provide the path to the PDF file with even-numbered pages (usually in reverse order): "
    )

    # Get the output file name and location from the user
    output_file = input("Enter the desired output PDF file name and path (e.g., output.pdf): ")

    merge_pdfs(odd_pages_file, even_pages_file, output_file)

    print(f"Successfully merged PDFs into {output_file}")


if __name__ == "__main__":
    main()
