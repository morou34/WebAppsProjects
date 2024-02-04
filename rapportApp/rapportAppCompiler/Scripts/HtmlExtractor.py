from docx2python import docx2python

DOC_DIR = 'file.docx'

# extract docx content
docx_content = docx2python(DOC_DIR)
# print(docx_content.text)

# extract docx content with basic font styles converted to html
with docx2python(DOC_DIR, html=True) as docx_content:
    print(docx_content.text)
 

# close file
docx_content.close()

 
