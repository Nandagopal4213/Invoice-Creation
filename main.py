import pandas  as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_no,date = filepath.split("-")

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8,txt=f"{invoice_no}",ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}")

    df= pd.read_excel(filepath, sheet_name="Sheet 1")
    for index, row in df.iterrows():
        pdf.set_font()
        pdf.set_text_color()
        pdf.cell()

    pdf.output(f"PDFs/{filename}.pdf")


