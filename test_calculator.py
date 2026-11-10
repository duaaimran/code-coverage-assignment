
import pytest
from calculator import calculate


def test_add():
    assert calculate("add", 5, 3) == 8


def test_subtract():
    assert calculate("subtract", 10, 4) == 6


def test_multiply():
    assert calculate("multiply", 3, 7) == 21


def test_divide():
    assert calculate("divide", 10, 2) == 5


def test_power():
    assert calculate("power", 2, 3) == 8


def test_modulus():
    assert calculate("modulus", 10, 3) == 1


def test_negative_numbers():
    assert calculate("add", -5, 2) == -3


def test_decimal_numbers():
    assert calculate("multiply", 2.5, 4) == 10
