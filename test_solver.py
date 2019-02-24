from typing import List, Tuple, Union

import pytest

from action import Action
from enums import BaseAction, Target
import solver
from type_aliases import BucketFilledState, BucketValueType


def to_tuples(actions: List[Tuple[Action, BucketFilledState]], target: Target) -> Tuple[List[Tuple[BaseAction, Target, BucketFilledState]], Target]:
    return [(action.base, action.target, current) for action, current in actions], target


def _solve(*args: Union[float, int]) -> Tuple[List[Tuple[BaseAction, Target, BucketFilledState]], Target]:
    """This is a wrapper around the solve function, which does two things:
    1. Returns a simpler set of objects for return type comparison
    2. Accepts ints for easier mypy type checking
    Both of these things are optional, but it makes writing and updating the tests better
    """
    return to_tuples(*solver.solve(*[BucketValueType(arg) for arg in args]))


def test_empty() -> None:
    assert ([], Target.Left) == _solve(0, 0, 0)
    assert ([], Target.Left) == _solve(1, 0, 0)
    assert ([], Target.Left) == _solve(0, 2, 0)
    assert ([], Target.Left) == _solve(5, 2, 0)


def test_simple_fill() -> None:
    assert ([(solver.BaseAction.Fill, solver.Target.Left, (1, 0))], Target.Left) == _solve(1, 5, 1)
    assert ([(solver.BaseAction.Fill, solver.Target.Right, (0, 5))], Target.Right) == _solve(1, 5, 5)


def assert_impossible() -> None:
    with pytest.raises(solver.UnsolvableError):
        _solve(5, 5, 3)


def test_532() -> None:
    assert ([
        (solver.BaseAction.Fill, solver.Target.Left, (5, 0)),
        (solver.BaseAction.Transfer, solver.Target.Right, (2, 3)),
    ], Target.Left) == _solve(5, 3, 2)


def test_one_and_half() -> None:
    assert ([
        (solver.BaseAction.Fill, solver.Target.Left, (2, 0)),
        (solver.BaseAction.Transfer, solver.Target.Right, (1.5, 0.5)),
    ], Target.Left) == _solve(2, 0.5, 1.5)


def test_534() -> None:
    assert ([
        (BaseAction.Fill, Target.Left, (5, 0)),
        (BaseAction.Transfer, Target.Right, (2, 3)),
        (BaseAction.Empty, Target.Right, (2, 0)),
        (BaseAction.Transfer, Target.Right, (0, 2)),
        (BaseAction.Fill, Target.Left, (5, 2)),
        (BaseAction.Transfer, Target.Right, (4, 3)),
    ], Target.Left) == _solve(5, 3, 4)


def test_53() -> None:
    with pytest.raises(solver.UnsolvableError):
        _solve(5, 3)
