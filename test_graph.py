from typing import Dict, Tuple, Optional

from action import Action
from enums import BaseAction, Target
from solver import generate_graph
from type_aliases import BucketValueType


def cleanup_generate(left: int, right:int) -> Dict[Tuple[int, int], Optional[Tuple[BaseAction, Target, Tuple[int, int]]]]:
    """Used to make mypy happier"""
    return {
        (int(key[0]), int(key[1])): ((value[0].base, value[0].target, (int(value[1][0]), int(value[1][1]))) if value else None)
        for key, value in generate_graph(BucketValueType(left), BucketValueType(right)).items()
    }


def test_01() -> None:
    graph = cleanup_generate(0, 1)
    assert graph == {
        (0, 0): None,
        (0, 1): (BaseAction.Fill, Target.Right, (0, 0)),
    }
