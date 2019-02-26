"""
This test class doesn't directly include graphs. It generates them from generate graphs.
It therefore (perhaps incorrectly), has that as a dependency
If any of these are failing, but test_graphs is also failing, fix those first.
"""

from dot import to_dot
from solver import generate_graph
from type_aliases import BucketValueType

# pylint: disable=missing-docstring  # Test file


def test_01() -> None:
    assert to_dot(generate_graph(BucketValueType(0), BucketValueType(1))) == """
digraph steps {
    l0r0 [label="(0, 0)"]
    l0r1 [label="(0, 1)"]
    l0r0 -> l0r1 [label="Fill Right"]
}"""


def test_011() -> None:
    assert to_dot(generate_graph(BucketValueType(0), BucketValueType(1)), BucketValueType(1)) == """
digraph steps {
    l0r0 [label="(0, 0)"]
    l0r1 [label="(0, 1)"][style=filled, fillcolor=lightgreen]
    l0r0 -> l0r1 [label="Fill Right"]
}"""
