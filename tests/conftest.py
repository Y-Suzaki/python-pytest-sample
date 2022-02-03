import sys
import os
from datetime import datetime
import pytest
from py.xml import html  # type: ignore
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))

import docstring_parser

print('Setup pytest.')
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../srcs/'))

def pytest_html_report_title(report):
    report.title = "単体テスト仕様書"

def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.insert(0, html.th("Tests"))
    cells.insert(1, html.th("Expects"))
    cells.append(html.th("Time", class_="sortable time", col="time"))

def pytest_html_results_table_row(report, cells):
    del cells[1:]
    cells.insert(0, html.td(report.tests))
    cells.insert(1, html.td(report.expects))
    cells.append(html.td(datetime.now(), class_="col-time"))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    print('******************************************************')
    print(report)
    docstring = docstring_parser.parse(str(item.function.__doc__))
    report.tests = docstring["Tests"]
    report.expects = docstring["Expects"]
