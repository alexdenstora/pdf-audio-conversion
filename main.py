import pdfplumber
import os

def extract_file_name(file_path):
    basename = os.path.basename(file_path)
    name, extension = os.path.splitext(basename)
    return name

def convert_to_text(file_path):
    name = extract_file_name(file_path)
    extension = ".txt"
    file_name = name + extension
    with pdfplumber.open(file_path) as pdf, open(file_name, "w", encoding="utf-8") as f:
        for page in pdf.pages:
            text = page.extract_text(x_tolerance=2) # lowered tolerance for identifying spaces between characters
            if text:
                f.write(text)
def main():
    pdf = "./Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf" # will change to user input
    convert_to_text(pdf)
        

if __name__ == "__main__":
    main()