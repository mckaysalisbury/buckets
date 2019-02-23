"""This just tests input checking. Doesn't check results. That is tested in test_solver.py"""
from main import main


def test_normal() -> None:
    assert 0 == main("1", "2", "3")


def test_non_integral() -> None:
    """I'm prety sure I can support floats, but it doesn't appear to be required, so I may drop these tests"""
    assert 0 == main("1.0", "2", "3")
    assert 0 == main("1.0", "2.0", "3.0")
    assert 0 == main("1.5", "2.5", "3.5")


def test_float() -> None:
    assert 0 == main("1.1", "2.1", "3.5")  # This doesn't work for float, because floating point numbers don't add together


def test_zeroes() -> None:
    assert 0 == main("0", "2", "3")
    assert 0 == main("2", "0", "3")
    assert 0 == main("0", "0", "3")
    assert 0 == main("1", "1", "0")
    assert 0 == main("0", "0", "0")


def test_letters() -> None:
    assert 1 == main("1a", "2", "3")
    assert 1 == main("1", "a", "3")
    assert 1 == main("1", "2", "a3")


def test_negative_bucket_sizes() -> None:
    assert 1 == main("-1", "1", "1")
    assert 1 == main("1", "-1", "1")
    assert 1 == main("1", "-1", "-1")
    assert 1 == main("-1", "-1", "-1")


def test_negative_water_size() -> None:
    assert 0 == main("0", "0", "-1")
    assert 0 == main("10", "10", "-1")
