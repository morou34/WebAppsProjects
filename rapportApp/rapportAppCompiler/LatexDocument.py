import os


class LaTeXDocument:
    def __init__(
        self,
        template,
        title,
        subtitle,
        names,
        program,
        program_specialization,
        course,
        department,
        submission_date,
        language,
        left_header,
        right_header,
        output_file="output.tex",
    ):
        self.latex_template = template
        self.title = title
        self.subtitle = subtitle
        self.names = names
        self.program = program
        self.program_specialization = program_specialization
        self.course = course
        self.department = department
        self.submission_date = submission_date
        self.language = language
        self.left_header = left_header
        self.right_header = right_header
        self.latex_code = ""
        self.output_file = output_file

        if self.latex_template:
            self.create_latex_structure()
            self.insert_content_from_file()
            self.save_to_file()

    def create_latex_structure(self):
        with open(self.latex_template, "r", encoding="utf-8") as file:
            self.latex_code = file.read()

        placeholders = {
            "__this_is_language_area__": self.language,
            "__this_is_left_header_area__": self.left_header,
            "__this_is_right_header_area__": self.right_header,
            "__this_is_title_area__": self.title,
            "__this_is_subtitle_area__": self.subtitle,
            "__this_is_names_area__": " \\\\ ".join(self.names),
            "__this_is_program_area__": self.program,
            "__this_is_program_specialization_area__": self.program_specialization,
            "__this_is_departement_area__": self.department,
            "__this_is_submission_date_area__": self.submission_date,
        }

        for placeholder, content in placeholders.items():
            self.latex_code = self.latex_code.replace(placeholder, content)

    def insert_content_from_file(self, fromdir="temp", filename="document_body.tex"):
        # Join the directory and filename to create the full path
        filepath = os.path.join(fromdir, filename)
        # Read the content of the txt file
        with open(filepath, "r", encoding="utf-8") as file:
            file_content = file.read()

        # Replace the placeholder in the latex code with the file content
        self.latex_code = self.latex_code.replace(
            "this_is_content_area_replaceMe", file_content
        )

    def save_to_file(self, savedir="LatexDocs"):
        # Join the directory and filename to create the full path

        filepath = os.path.join(savedir, self.output_file)

        # Check if a file with the same name already exists
        if os.path.exists(filepath):
            # Delete the existing file
            os.remove(filepath)
            print(f"Existing file '{filepath}' was removed.")

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(self.latex_code)

        print(f"LaTeX document {self.output_file} saved to {filepath}")
