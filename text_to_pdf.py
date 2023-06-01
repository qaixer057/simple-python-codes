# Reference
# https://github.com/reingart/pyfpdf/blob/master/docs/Tutorial.md
# refer to manual for further PDF formatting
from fpdf import FPDF
with open('email.txt', 'r') as file:
    text = file.read()

lines = text.split('\n')

pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', size=12)

for line in lines:
    pdf.cell(0, 10, txt=line,align='J', ln=True)

print("Writing PDF files.")
pdf.output('output3.pdf')
print("Done.! writing PDF file.")
