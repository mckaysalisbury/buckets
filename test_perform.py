"""Tests the `perform` function (which performs the actions)"""
from typing import Callable, Tuple

from action import Action
from enums import BaseAction, Target
from performer import get_performer
from type_aliases import BucketValueType, BucketFilledState

# pylint: disable=missing-docstring  # Test file


def _wrap_performer(
        left: int,
        right: int
    ) -> Callable[[Action, Tuple[int, int]], BucketFilledState]:
    """
    This function wraps the existing behavior so that it passes mypy.
    It is designed to be a drop in place replacement for get_performer
    """
    performer = get_performer(BucketValueType(left), BucketValueType(right))
    def wrapper(action: Action, input_state: Tuple[int, int]) -> BucketFilledState:
        return performer(action, (BucketValueType(input_state[0]), BucketValueType(input_state[1])))
    return wrapper


def test_empty() -> None:
    perform = _wrap_performer(3, 5)
    assert (3, 0) == perform(Action(BaseAction.Empty, Target.Right), (3, 5))
    assert (0, 5) == perform(Action(BaseAction.Empty, Target.Left), (3, 5))


def test_fill() -> None:
    perform = _wrap_performer(3, 5)
    assert (0, 5) == perform(Action(BaseAction.Fill, Target.Right), (0, 0))
    assert (3, 0) == perform(Action(BaseAction.Fill, Target.Left), (0, 0))
    assert (3, 1) == perform(Action(BaseAction.Fill, Target.Left), (1, 1))


def test_transfer() -> None:
    perform = _wrap_performer(3, 5)
    assert (0, 0) == perform(Action(BaseAction.Transfer, Target.Left), (0, 0))
    assert (1, 0) == perform(Action(BaseAction.Transfer, Target.Left), (1, 0))
    assert (1, 0) == perform(Action(BaseAction.Transfer, Target.Left), (0, 1))
    assert (3, 3) == perform(Action(BaseAction.Transfer, Target.Left), (2, 4))
    assert (0, 0) == perform(Action(BaseAction.Transfer, Target.Right), (0, 0))
    assert (0, 1) == perform(Action(BaseAction.Transfer, Target.Right), (1, 0))
    assert (0, 1) == perform(Action(BaseAction.Transfer, Target.Right), (0, 1))
    assert (1, 5) == perform(Action(BaseAction.Transfer, Target.Right), (2, 4))
