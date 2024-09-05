# PDF Merger Script

This Python script merges all PDF files located in a specified folder into a single PDF file. It uses the `PyPDF2` library to combine the PDFs, making it easy to concatenate multiple PDF files into one.

## Requirements

Before running the script, you need to install the required library:

```bash
pip install PyPDF2
```

## Function Description

### `merge_pdfs_in_folder(folder_path, output_filename)`

This function merges all PDF files in a given folder into a single output PDF.

### Parameters:

- **folder_path**: (str) The path to the folder that contains the PDFs you want to merge.
- **output_filename**: (str) The name (or path) of the output PDF file where the merged content will be saved.

### How It Works:

1. The function scans the specified `folder_path` for all `.pdf` files.
2. It sorts the files alphabetically to ensure consistent ordering (you can modify this behavior if necessary).
3. Each PDF is opened, appended to the merger object, and processed sequentially.
4. The combined content is then saved as a single PDF to the specified `output_filename`.