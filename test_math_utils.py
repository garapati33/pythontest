import pytest
from MathUtils import MathUtils

@pytest.mark.parametrize("a, b, expected_sum", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (1000, 500, 1500),
])
def test_add(a, b, expected_sum):
    assert MathUtils.add(a, b) == expected_sum

@pytest.mark.parametrize("a, b, expected_difference", [
    (5, 2, 3),
    (-1, -1, 0),
    (0, 0, 0),
    (100, 50, 50),
])
def test_subtract(a, b, expected_difference):
    assert MathUtils.subtract(a, b) == expected_difference

@pytest.mark.parametrize("a, b, expected_product", [
    (5, 2, 10),
    (-1, -1, 1),
    (0, 0, 0),
    (10, 10, 100),
])
def test_multiply(a, b, expected_product):
    assert MathUtils.multiply(a, b) == expected_product

@pytest.mark.parametrize("a, b, expected_result", [
    (10, 2, 5),
    (-10, 2, -5),
    (0, 5, 0),
    (10, 0, -1.0),  # division by zero
])
def test_divide(a, b, expected_result):
    assert MathUtils.divide(a, b) == expected_result
