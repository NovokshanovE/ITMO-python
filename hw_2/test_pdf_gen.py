
from latex_gen import generate_latex_table, generate_latex_image
import os

example_matrix = [
    ["Row1Col1", "Row1Col2", "Row1Col3"],
    ["Row2Col1", "Row2Col2", "Row2Col3"],
    ["Row3Col1", "Row3Col2", "Row3Col3"]
]
table_code = generate_latex_table(example_matrix)

image_code = generate_latex_image('artifacts/test_image.png')

full_latex_document = f"""
\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{graphicx}}

\\begin{{document}}

{table_code}
{image_code}

\\end{{document}}
"""

with open('artifacts/generated_document.tex', 'w', encoding='utf-8') as f:
    f.write(full_latex_document)

os.system('pdflatex -output-directory=artifacts artifacts/generated_document.tex')
