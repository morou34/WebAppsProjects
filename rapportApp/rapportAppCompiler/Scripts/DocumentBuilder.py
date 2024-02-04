from docx import Document
from DocumentStructure import (
    DocumentWrapper,
    SectionOne,
    SectionTwo,
    SectionThree,
    SectionFour,
    SectionFive,
)


def build_structure(docx_file):
    document = DocumentWrapper()

    # Current section references for each level
    current_sections = [None, None, None, None, None]
    latest_active_lvl = None
    levels = [0, 1, 2, 3, 4]

    for paragraph in docx_file.paragraphs:
        level = None
        content = paragraph.text.strip()

        if paragraph.style.name == "Heading 1":
            level = 0
            if latest_active_lvl is None:
                latest_active_lvl = 0
            section = SectionOne(content, "")
        elif paragraph.style.name == "Heading 2":
            level = 1
            latest_active_lvl = 1
            section = SectionTwo(content, "")
        elif paragraph.style.name == "Heading 3":
            level = 2
            latest_active_lvl = 2
            section = SectionThree(content, "")
        elif paragraph.style.name == "Heading 4":
            level = 3
            latest_active_lvl = 3
            section = SectionFour(content, "")
        elif paragraph.style.name == "Heading 5":
            level = 4
            latest_active_lvl = 4
            section = SectionFive(content, "")

        if level is not None:
            current_sections[level] = section
            # Check if there is a parent section and append
            if level > 0 and current_sections[level - 1] is not None:
                current_sections[level - 1].sections.append(section)
            elif level == 0:
                document.body.sections.append(section)
        else:
            print(f"{latest_active_lvl}-{content}")
            # Check if there is a current section to append the content
            if (
                latest_active_lvl in levels
                and current_sections[latest_active_lvl] is not None
            ):
                current_sections[latest_active_lvl].content += f"{content}"

    return document



