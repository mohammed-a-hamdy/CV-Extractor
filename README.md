# CV_Extractor

## Module Overview
The CV_Extractor module provides functions to extract relevant information from a collection of CVs in PDF and DOC formats. It utilizes the Pandas, SpaCy, PyPDF2, and docx2txt libraries to perform text extraction, named entity recognition, and regular expression matching. The extracted information, including first name, last name, email, LinkedIn URL, and file path, is then saved in an Excel file for further analysis.

## Functional Units

### `extract_text_from_doc(file_path)`
Extracts plain text content from a DOC file.

**Inputs:**
- `file_path` (str): The path to the DOC file.

**Outputs:**
- `text_content` (str): The extracted plain text content.

### `extract_text_from_pdf(pdf_path)`
Extracts plain text content from a PDF file.

**Inputs:**
- `pdf_path` (str): The path to the PDF file.

**Outputs:**
- `extracted_text` (str): The extracted plain text content.

### `split_full_name(full_name)`
Splits a full name into first name and last name.

**Inputs:**
- `full_name` (str): The full name to be split.

**Outputs:**
- `first_name` (str): The extracted first name.
- `last_name` (str): The extracted last name.

### `extract_information(text, path)`
Extracts relevant information (first name, last name) from a text using named entity recognition.

**Inputs:**
- `text` (str): The text to be processed.
- `path` (str): The file path associated with the text (used for testing purposes).

**Outputs:**
- `f_name` (str): The extracted first name.
- `l_name` (str): The extracted last name.

### `extract_information_re(text)`
Extracts email and LinkedIn URL from a text using regular expression matching.

**Inputs:**
- `text` (str): The text to be processed.

**Outputs:**
- `email` (str): The extracted email.
- `linkedin_url` (str): The extracted LinkedIn URL.

### `save(f_name, l_name, email, linkedin_url, paths)`
Saves the extracted information in an Excel file.

**Inputs:**
- `f_name` (list): The list of first names.
- `l_name` (list): The list of last names.
- `email` (list): The list of emails.
- `linkedin_url` (list): The list of LinkedIn URLs.
- `paths` (list): The list of file paths.

**Outputs:**
- None.

### `loop_over_cvs_pdf(dir)`
Returns a list of PDF file paths within a specified directory.

**Inputs:**
- `dir` (str): The directory path.

**Outputs:**
- `pdf_paths` (list): The list of PDF file paths.

### `loop_over_cvs_doc(dir)`
Returns a list of file paths within a specified directory.

**Inputs:**
- `dir` (str): The directory path.

**Outputs:**
- `doc_paths` (list): The list of DOC file paths.

## Script-level Usage

1. Initialize the `dir` variable with the path to the directory containing the CV files.
2. Call the `loop_over_cvs_pdf` function to retrieve a list of PDF file paths within the directory.
3. Iterate over the PDF file paths and extract information using the `extract_information` and `extract_information_re` functions.
4. Append the extracted information to the respective lists: `f_names`, `l_names`, `emails`, `paths`, and `linkedin_urls`.
5. Call the `save` function to save the extracted information in an Excel file.
6. Call the `loop_over_cvs_doc` function to retrieve a list of DOC file paths within the directory.
7. Repeat steps 3-5 for the DOC file paths.
8. The extracted information will be saved in the `CVs.xlsx` Excel file.

**Note:** This documentation assumes that the required libraries (pandas, spacy, os, re, PyPDF2, docx2txt) have been installed and imported.