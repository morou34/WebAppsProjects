from docx import Document
doc = Document("test.docx")
for para in doc.paragraphs:
     print(para.text)