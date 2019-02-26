"""This just tests input checking. Doesn't check results. That is tested in test_solver.py"""
import sys

import pytest

from main import main

# pylint: disable=missing-docstring  # Test file

def _test_main(*args: str):
    sys.argv = ['test'] + list(args)
    main()


def test_normal() -> None:
    _test_main("1", "2", "3")


def test_non_integral() -> None:
    _test_main("1.0", "2", "3")
    _test_main("1.0", "2.0", "3.0")
    _test_main("1.5", "2.5", "3.5")


def test_non_float() -> None:
    _test_main("1.1", "2.1", "3.5")


def test_zeroes() -> None:
    _test_main("0", "2", "3")
    _test_main("2", "0", "3")
    _test_main("0", "0", "3")
    _test_main("1", "1", "0")
    _test_main("0", "0", "0")


def test_letters() -> None:
    with pytest.raises(SystemExit):
        _test_main("1a", "2", "3")
    with pytest.raises(SystemExit):
        _test_main("1", "a", "3")
    with pytest.raises(SystemExit):
        _test_main("1", "2", "a3")


def test_negative_bucket_sizes() -> None:
    with pytest.raises(SystemExit):
        _test_main("-1", "1", "1")
    with pytest.raises(SystemExit):
        _test_main("1", "-1", "1")
    with pytest.raises(SystemExit):
        _test_main("1", "-1", "-1")
    with pytest.raises(SystemExit):
        _test_main("-1", "-1", "-1")


def test_negative_water_size() -> None:
    _test_main("0", "0", "-1")
    _test_main("10", "10", "-1")


def test_bad_args() -> None:
    with pytest.raises(SystemExit):
        _test_main()
    with pytest.raises(SystemExit):
        _test_main("1")
    with pytest.raises(SystemExit):
        _test_main("a")
    with pytest.raises(SystemExit):
        _test_main("1", "a")
    with pytest.raises(SystemExit):
        _test_main("1", "2", "3", "4")
    with pytest.raises(SystemExit):
        _test_main("1", "2", "3", "4", "5")


def test_two_args() -> None:
    _test_main("5", "3")


def test_strange_options() -> None:
    with pytest.raises(SystemExit):
        _test_main("--what")
    with pytest.raises(SystemExit):
        _test_main("5", "3", "--what")
    with pytest.raises(SystemExit):
        _test_main("5", "3", "4", "--what")


def test_graph() -> None:
    _test_main("5", "3", "--graph")


def test_verbose_graph() -> None:
    _test_main("5", "3", "--graph", "--verbose")
    _test_main("5", "3", "4", "--graph", "--verbose")


def test_verbose_not_graph() -> None:
    # I don't have a preference what this does, as long as it doesn't crash
    _test_main("5", "3", "--verbose")
    _test_main("5", "3", "4", "--verbose")
