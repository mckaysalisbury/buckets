"""This just tests input checking. Doesn't check results. That is tested in test_solver.py"""
from main import main

# pylint: disable=missing-docstring  # Test file


def test_normal() -> None:
    assert main("1", "2", "3") == 0


def test_non_integral() -> None:
    assert main("1.0", "2", "3") == 0
    assert main("1.0", "2.0", "3.0") == 0
    assert main("1.5", "2.5", "3.5") == 0


def test_non_float() -> None:
    assert main("1.1", "2.1", "3.5") == 0


def test_zeroes() -> None:
    assert main("0", "2", "3") == 0
    assert main("2", "0", "3") == 0
    assert main("0", "0", "3") == 0
    assert main("1", "1", "0") == 0
    assert main("0", "0", "0") == 0


def test_letters() -> None:
    assert main("1a", "2", "3") == 1
    assert main("1", "a", "3") == 1
    assert main("1", "2", "a3") == 1


def test_negative_bucket_sizes() -> None:
    assert main("-1", "1", "1") == 1
    assert main("1", "-1", "1") == 1
    assert main("1", "-1", "-1") == 1
    assert main("-1", "-1", "-1") == 1


def test_negative_water_size() -> None:
    assert main("0", "0", "-1") == 0
    assert main("10", "10", "-1") == 0


def test_bad_args() -> None:
    assert main() == 1
    assert main("1") == 1
    assert main("a") == 1
    assert main("1", "2", "3", "4") == 1
    assert main("1", "2", "3", "4", "5") == 1


def test_two_args() -> None:
    assert main("5", "3") == 0


def test_strange_options() -> None:
    assert main("--what") == 1
    assert main("5", "3", "--what") == 1
    assert main("5", "3", "4", "--what") == 1


def test_graph() -> None:
    assert main("5", "3", "--graph") == 0
