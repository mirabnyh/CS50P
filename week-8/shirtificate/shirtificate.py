from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Helvetica")
pdf.set_page_background((252,212,255))
pdf.set_font('helvetica', size=12)
pdf.cell(text=name)
pdf.output("shirtificate.pdf")
