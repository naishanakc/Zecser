import os
from parsers.resume_parser.pdf_reader import read_pdf
from parsers.resume_parser.docx_reader import read_docx
from parsers.resume_parser.cleaner import clean_text


def extract_resume(file_path):

    if file_path.endswith(".pdf"):
        raw = read_pdf(file_path)

    elif file_path.endswith(".docx"):
        raw = read_docx(file_path)

    else:
        raise Exception("Unsupported file")

    return clean_text(raw)


def extract_folder(input_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith(".pdf") or file.endswith(".docx"):

            path = os.path.join(input_dir, file)
            cleaned = extract_resume(path)

            out = os.path.join(output_dir, file.split(".")[0] + ".txt")

            with open(out, "w", encoding="utf8") as f:
                f.write(cleaned)

            print("Processed:", file)