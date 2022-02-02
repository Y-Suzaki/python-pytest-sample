import sys
import os
from py.xml import html  # type: ignore

print('Setup pytest.')
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../srcs/'))

def pytest_html_report_title(report):
    report.title = "My very own title!"

def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.insert(0, html.th("Tests"))
    cells.insert(1, html.th("Expects"))
    cells.append(html.th("Time", class_="sortable time", col="time"))
