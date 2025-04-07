from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
import os

def pdf_to_html(pdf_path, output_html_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as f:
        extract_text_to_fp(f, output_string, laparams=LAParams(), output_type='html', codec=None)
    
    with open(output_html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(output_string.getvalue())

# Example usage
pdf_path = "C:/Users/shiva/Downloads/Summary.pdf"
output_html_path = 'C:/Users/shiva/Downloads/output.html'
pdf_to_html(pdf_path, output_html_path)



# import fitz  # PyMuPDF

# def pdf_to_html_fitz(pdf_path, output_html_path):
#     doc = fitz.open(pdf_path)
#     html_content = ''
    
#     for page in doc:
#         html_content += page.get_text('html')

#     with open(output_html_path, 'w', encoding='utf-8') as f:
#         f.write(html_content)

# # Usage
# pdf_to_html_fitz(""C:\Users\shiva\Downloads\sort.html"", "C:/Users/shiva/Downloads/file.html")
