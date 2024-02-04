from docx import Document
from utils import showStructure
from DocumentStructure import (
    DocumentWrapper,
    DocumentBody,
    SectionOne,
    SectionTwo,
    SectionThree,
)

file = "docs/test.docx"
document = Document(file)

# for paragraph in document.paragraphs:
#     if paragraph.style.name == 'Heading 1':
#         print(f'- {paragraph.text}')
#     if paragraph.style.name == 'Heading 2':
#         print(f'--- {paragraph.text}')
#     if paragraph.style.name == 'Heading 3':
#         print(f'------ {paragraph.text}')
#     if paragraph.style.name == 'Heading 4':
#         print(f'--------- {paragraph.text}')
#     if paragraph.style.name == 'Heading 5':
#         print(f'------------ {paragraph.text}')


# Example Usage
mydocument = DocumentWrapper(title="TP1", course="Deep learning")
section1 = SectionOne(
    "1. Introduction", "This is the introduction for the deep learning course."
)
section2 = SectionOne(
    "2. Analyse", "This is the introduction for the deep learning course."
)
section1_1 = SectionTwo(
    "1.1. History", "History information about the deep learning course."
)
section1_2 = SectionTwo(
    "1.2. Background", "Background information about the deep learning course."
)

section1.sections.append(section1_1)
section1.sections.append(section1_2)
mydocument.body.sections.append(section1)
mydocument.body.sections.append(section2)

# print_document_structure(mydocument.body)

# Example usage of the modified class
doc = DocumentWrapper(
    title="TP 2: Deep Learning", subtitle="An Example", authors=["John Doe", "Jane Doe"]
)

mydocument.printDoc(onlyStructure=False)
# print(mydocument)

# help(DocumentWrapper.__str__)
# help(DocumentWrapper.printDoc)
