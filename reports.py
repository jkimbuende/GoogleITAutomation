#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
report = SimpleDocTemplate("/tmp/processed.pdf")

def generate_report(attachment, title, paragraph):
  from reportlab.lib.styles import getSampleStyleSheet
  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report_table = Paragraph(paragraph, styles['BodyText'])
  report.build( [report_title, report_table] )
