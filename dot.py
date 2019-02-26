"""Turns graphs into dot files aka graphviz"""
from type_aliases import BucketFilledState, BucketValueType, Graph

from action import Action


def _name(state: BucketFilledState) -> str:
    return f'l{state[0]}r{state[1]}'


def _state_label(state: BucketFilledState) -> str:
    return f'({state[0]}, {state[1]})'


def _link_label(action: Action) -> str:
    return f'{action.base.name} {action.target.name}'


HIGHLIGHT = '[style=filled, fillcolor=lightgreen]'

def _state_row(state: BucketFilledState, target: BucketValueType = BucketValueType(-1)) -> str:
    return f'{_name(state)} [label="{_state_label(state)}"]{HIGHLIGHT if target in state else ""}'


def _link_row(state: BucketFilledState, action: Action, parent: BucketFilledState) -> str:
    return f'{_name(parent)} -> {_name(state)} [label="{_link_label(action)}"]'


def to_dot(graph: Graph, target: BucketValueType = BucketValueType(-1)) -> str:
    """Converts a bucket graph into a DOT graph"""

    return f"""
digraph steps {{
    {r'''
    '''.join(_state_row(state, target) for state in graph.keys())}
    {r'''
    '''.join(_link_row(state, *value) for state, value in graph.items() if value)}
}}"""
