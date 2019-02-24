"""
This test class doesn't type out graphs. It generates them from generate graphs.
It therefore (perhaps incorrectly), has that as a dependency
If any of these are failing, but test_graphs is also failing, fix those first.
"""

from dot import to_dot
from solver import generate_graph
from type_aliases import BucketValueType


def test_01() -> None:
    assert """
digraph steps {
    l0r0 [label="(0, 0)"]
    l0r1 [label="(0, 1)"]
    l0r0 -> l0r1
}""" == to_dot(generate_graph(BucketValueType(0), BucketValueType(1)))
