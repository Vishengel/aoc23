import pytest
from .puzzle2 import is_invalid_complex

@pytest.mark.parametrize("input, expected",
                         [("111111", True),
                          ("12121212", True),
                          ("100410041004", True),
                          ("123456123456", True),
                          ("123123123123", True),
                          ("1", False),
                          ])
def test_is_invalid_complex(input, expected):
    assert (is_invalid_complex(input) == expected)