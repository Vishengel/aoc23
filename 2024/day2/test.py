import pytest

from .puzzle2 import report_is_safe, report_is_safe_with_dampener, Report, transposition_table


def test_parse_report():
    report = "51 48 46 43 42 41 38 36"
    assert report_is_safe(report) == True

@pytest.mark.parametrize(("report", "is_safe"),
                         [(Report("4 3 4 5 6"), True),
                          (Report("89 90 88 90 94"), False)])
def test_report_is_safe_with_dampener(report, is_safe):
    assert report_is_safe_with_dampener(report) == is_safe
    print(transposition_table)