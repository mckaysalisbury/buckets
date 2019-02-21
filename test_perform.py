from action import Action
from enums import BaseAction, Target
from performer import get_performer


def test_empty() -> None:
    perform = get_performer(3, 5)
    assert (3, 0) == perform(Action(BaseAction.Empty, Target.Right), (3, 5))
    assert (0, 5) == perform(Action(BaseAction.Empty, Target.Left), (3, 5))


def test_fill() -> None:
    perform = get_performer(3, 5)
    assert (0, 5) == perform(Action(BaseAction.Fill, Target.Right), (0, 0))
    assert (3, 0) == perform(Action(BaseAction.Fill, Target.Left), (0, 0))
    assert (3, 1) == perform(Action(BaseAction.Fill, Target.Left), (1, 1))


def test_transfer() -> None:
    perform = get_performer(3, 5)
    assert (0, 0) == perform(Action(BaseAction.Transfer, Target.Left), (0, 0))
    assert (1, 0) == perform(Action(BaseAction.Transfer, Target.Left), (1, 0))
    assert (1, 0) == perform(Action(BaseAction.Transfer, Target.Left), (0, 1))
    assert (3, 3) == perform(Action(BaseAction.Transfer, Target.Left), (2, 4))
    assert (0, 0) == perform(Action(BaseAction.Transfer, Target.Right), (0, 0))
    assert (0, 1) == perform(Action(BaseAction.Transfer, Target.Right), (1, 0))
    assert (0, 1) == perform(Action(BaseAction.Transfer, Target.Right), (0, 1))
    assert (1, 5) == perform(Action(BaseAction.Transfer, Target.Right), (2, 4))
