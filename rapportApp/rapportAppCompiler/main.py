import os
import sys
import shutil
import time
from datetime import datetime
from DocumentStructure import DocumentWrapper
from docx import Document
from LatexDocument import LaTeXDocument
from Scripts.utils import run_pdflatex, clean_files
from Scripts.constants import *

# Record the start time
start_time = time.time()

# Check if docs directory exists, if not create it
docs_dir = "docs"
if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

# main args
if len(sys.argv) > 1:
    # Original document path provided as command-line argument
    original_doc_path = sys.argv[1]

    # Safety check: Ensure the file exists before proceeding
    if not os.path.isfile(original_doc_path):
        print(f"The specified file does not exist: {original_doc_path}")
        sys.exit()
    # Extracting the file name and extension
    doc_name, doc_extension = os.path.splitext(os.path.basename(original_doc_path))
    # Generate a date-time string
    datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S_")
    # New file name with date-time appended
    new_doc_name = f"{doc_name}_{datetime_str}{doc_extension}"
    # New path in the docs directory
    doc_file_path = os.path.join(docs_dir, new_doc_name)
    # Copy the document to the docs directory with the new file name
    shutil.copy2(original_doc_path, doc_file_path)
else:
    print("Please provide a path to the document to convert to PDF.")
    sys.exit()

# Proceed with document processing
mydocument = DocumentWrapper(path_to_file=doc_file_path)
# mydocument.printDoc()
OUTPUT_FILE_NAME = new_doc_name.replace("_.docx", ".tex")
doc = LaTeXDocument(
    template=TEMPLATE_FILE_PATH,
    title=TITLE,
    subtitle=SUBTITLE,
    names=NAMES,
    program=PROGRAM,
    program_specialization=PROGRAM_SPECIALIZATION,
    course=COURSE,
    department=DEPARTEMENT,
    submission_date=SUBMISSION_DATE,
    language=LANGUAGE,
    left_header=LEFT_HEADER,
    right_header=RIGHT_HEADER,
    output_file=OUTPUT_FILE_NAME,
)

tex_input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE_NAME)
for times in range(1, 2):
    run_pdflatex(tex_input_file_path)
    print(f"pdf is compiled {times} times.")

# Clean up after LatexPDF
clean_files(OUTPUT_DIR)
clean_files(IMAGES_DIR)

# Record the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time

print(f"The code took {duration:.2f} seconds to finish.")

# Check if the pdf was compiled succesfully
pdf_file = OUTPUT_FILE_NAME.replace('.tex', '.pdf')
ouput_file_path = os.path.join(docs_dir, pdf_file)
if not os.path.isfile(ouput_file_path):
        print(f"The file was not compiled successfully.")
        sys.exit()
