import os
import PyPDF2

def merge_pdfs_in_folder(folder_path, output_filename):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Sort the PDF files
    pdf_files.sort()
   
    for i in pdf_files:
        print(i)
    # Loop through the list of PDFs and append them to the merger object
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        with open(pdf_path, 'rb') as file:
            pdf_merger.append(file)

    # Write the combined PDF to an output file
    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f"Merged {len(pdf_files)} PDFs from {folder_path} into {output_filename}")


folder_path = "D:\output\input"  # Folder containing PDFs
output_pdf = "D:\output\l1.pdf"  # Output PDF filename

merge_pdfs_in_folder(folder_path, output_pdf)
