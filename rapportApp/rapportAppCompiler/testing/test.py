from docx import Document
import re

def clean_caption(caption):
    # Regular expression pattern to match table captions and numbers
    pattern = r'^(tableau|table|tab\.|tabelle|tabla|tabel)[\s]*[\d]*[\s]*[:]*[\s]*'
    # Remove the matched patterns and return the cleaned caption
    return re.sub(pattern, '', caption, flags=re.IGNORECASE).strip()

# Load the document
doc = Document("test.docx")

# Define a broader list of elements that might be used for table captions
elements_to_search = ['table', 'tableau', 'tab.', 'tabelle', 'tabla', 'tabel']  # Add more as needed

table_index = 1 
tables = {}
place_holder = 'place_holder'
# Loop through each paragraph and check if any element is at the beginning
for para in doc.paragraphs:
    if para.text:  # Checks if para.text is not None or empty
        # Strip leading/trailing spaces and convert to lower case
        text = para.text.strip().lower()
        if any(text.startswith(element) for element in elements_to_search):
            caption = clean_caption(para.text)
            tables[table_index] = [place_holder, caption]
            table_index += 1

# Print the extracted table captions

for index, caption in tables.items():
    print(f"Table {index}: {caption}")
