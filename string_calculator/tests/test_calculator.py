import pytest
from string_calculator.calculator import add

@pytest.mark.parametrize(
    "stringnumber,expected",
    [("", 0), ("1,1", 2), ("1",1)],
)
def test_add_should_return_the_sum(
    stringnumber, expected
):
    assert add(stringnumber) == expected, "Error, wrong addition of integers"

@pytest.mark.parametrize(
    "stringnumber,expected",
    [("1,2,3,4", 10),("10,2,3,44",59)],
)
def test_add_of_multiple_interges(
    stringnumber, expected
):
    assert add(stringnumber) == expected, "Error, wrong addition of multiple integers"


@pytest.mark.parametrize(
    "stringnumber,expected",
    [("1\n2,3", 6),("10\n8",18)],
)
def test_add_of_escape_char(
    stringnumber, expected
):
    assert add(stringnumber) == expected, "Error, did not take care of escape char"

@pytest.mark.parametrize(
    "stringnumber,expected",
    [("//;\n1;2", 3),("//4\n148",9)],
)
def test_add_of_different_delimiters(
    stringnumber, expected
):
    assert add(stringnumber) == expected, "Error, did not take care of delimiter"

@pytest.mark.parametrize(
    "stringnumber,expected",
    [("//;\n1000;1;2", 3),("1000",0)],
)
def test_add_of_1000(
    stringnumber, expected
):
    assert add(stringnumber) == expected, "Error, did not take care of 1000"