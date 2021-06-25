#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

'''To generate pdf report with filename, title and table of data'''
def generate(filename, title, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    table_style = [('FONTNAME', (0,0), (-1,-1), "Helvetica"),
                    ('ALIGN', (0,0), (-1,-1), "LEFT")]
    report_table = Table(data=table_data, style=table_style,hAlign="LEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_table])
