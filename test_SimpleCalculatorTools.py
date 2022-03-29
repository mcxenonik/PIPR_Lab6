from SimpleCalculatorTools import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(5, 10) == 15


def test_subtract():
    assert subtract(30, 17) == 13


def test_subtract_negative_result():
    assert subtract(10, 13) == -3


def test_subtract_negative_operands():
    assert subtract(-5, -7) == 2


def test_subtract_zero_operands():
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(5, 7) == 35


def test_multiply_negative_operand():
    assert multiply(6, -8) == -48


def test_multiply_negative_operands():
    assert multiply(-9, -8) == 72


def test_multiply_zero_operand():
    assert multiply(10, 0) == 0


def test_divide():
    assert divide(81, 9) == 9


def test_divide_float_result():
    assert divide(10, 3) == pytest.approx(3.33, rel=1e-2)


def test_divide_negative_operand():
    assert divide(-50, 10) == -5


def test_divide_negative_operands():
    assert divide(-32, -8) == 4


def test_divide_zero_first_operand():
    assert divide(0, 10) == 0


def test_divide_zero_second_operand():
    with pytest.raises(ZeroDivisionError):
        divide(45, 0)
