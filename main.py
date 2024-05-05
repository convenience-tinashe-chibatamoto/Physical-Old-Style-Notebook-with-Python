from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

try:
    pdf.add_font("Poppins", "", "Poppins-Regular.ttf", uni=True)
    pdf.add_font("Poppins", "B", "Poppins-Medium.ttf", uni=True)
    chosen_font = "Poppins"
    print("Poppins Font Loaded Successfully\n")
except RuntimeError as inst:
    print(inst.args[0] + " | Using Arial font as default\n")
    chosen_font = "Arial"

df = pd.read_csv("topics.csv")
print(f"{df.index.max() + 1} Sections to be created\n")

for index, row in df.iterrows():
    print(f"{index + 1}. {row['Topic']} | Section Created")
    for x in range(row["Pages"]):
        pdf.add_page()

        # Header Config
        pdf.set_font(family=chosen_font, style="B", size=16)
        pdf.set_text_color(19, 38, 47)
        pdf.set_draw_color(230, 230, 85)
        pdf.set_line_width(1)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="L", ln=1, border=0)
        pdf.line(10, 20, 200, 20)

        # Line Config
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.1)
        for line in range(30, 280, 10):
            pdf.line(10, line, 200, line)

        # Footer Config
        pdf.set_line_width(0.5)
        pdf.line(10, 280, 200, 280)
        pdf.ln(260)
        pdf.set_font(family=chosen_font, style="", size=8)
        pdf.cell(
            w=0,
            h=8,
            txt=f"{row['Topic']} | Page {x + 1} of {row['Pages']}",
            align="R",
            ln=1,
            border=0
        )

# Export PDF file
pdf.output("output.pdf")
print("")
print("PDF Created Successfully")