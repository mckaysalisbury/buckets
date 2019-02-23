from typing import List, Tuple

import pytest

from action import Action
from enums import BaseAction, Target
import solver
from type_aliases import BucketFilledState


def to_tuples(actions: List[Tuple[Action, BucketFilledState]], target: Target) -> Tuple[List[Tuple[BaseAction, Target, BucketFilledState]], Target]:
    return [(action.base, action.target, current) for action, current in actions], target


def test_empty() -> None:
    assert ([], Target.Left) == solver.solve(0, 0, 0)
    assert ([], Target.Left) == solver.solve(1, 0, 0)
    assert ([], Target.Left) == solver.solve(0, 2, 0)
    assert ([], Target.Left) == solver.solve(5, 2, 0)


def test_simple_fill() -> None:
    assert ([(solver.BaseAction.Fill, solver.Target.Left, (1, 0))], Target.Left) == to_tuples(*solver.solve(1, 5, 1))
    assert ([(solver.BaseAction.Fill, solver.Target.Right, (0, 5))], Target.Right) == to_tuples(*solver.solve(1, 5, 5))


def assert_impossible() -> None:
    with pytest.raises(solver.UnsolvableError):
        solver.solve(5, 5, 3)


def test_532() -> None:
    assert ([
        (solver.BaseAction.Fill, solver.Target.Left, (5, 0)),
        (solver.BaseAction.Transfer, solver.Target.Right, (2, 3)),
    ], Target.Left) == to_tuples(*solver.solve(5, 3, 2))


# def test_one_and_half() -> None:
#     assert ([
#         (solver.BaseAction.Fill, solver.Target.Left, (2, 0)),
#         (solver.BaseAction.Transfer, solver.Target.Right, (1.5, 0.5)),
#     ], Target.Left) == to_tuples(*solver.solve(2, 0.5, 1.5))


def test_534() -> None:
    assert ([
        (BaseAction.Fill, Target.Left, (5, 0)),
        (BaseAction.Transfer, Target.Right, (2, 3)),
        (BaseAction.Empty, Target.Right, (2, 0)),
        (BaseAction.Transfer, Target.Right, (0, 2)),
        (BaseAction.Fill, Target.Left, (5, 2)),
        (BaseAction.Transfer, Target.Right, (4, 3)),
    ], Target.Left) == to_tuples(*solver.solve(5, 3, 4))