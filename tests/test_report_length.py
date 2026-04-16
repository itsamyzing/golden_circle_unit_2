from lib.report_length import *

def test_report_length_basic():
    result = report_length("hello")
    assert result == "This string was 5 characters long"

def test_report_length_shorter():
    result = report_length("amy")
    assert result == "This string was 3 characters long"

def test_report_length_longer():
    result = report_length("washington")
    assert result == "This string was 10 characters long"