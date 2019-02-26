"""Turns graphs into dot files aka graphviz"""
from type_aliases import BucketFilledState, Graph

from action import Action


def _name(state: BucketFilledState) -> str:
    return f'l{state[0]}r{state[1]}'


def _state_label(state: BucketFilledState) -> str:
    return f'({state[0]}, {state[1]})'


def _link_label(action: Action) -> str:
    return f'{action.base.name} {action.target.name}'


def _state_row(state: BucketFilledState) -> str:
    return f'{_name(state)} [label="{_state_label(state)}"]'


def _link_row(state: BucketFilledState, action: Action, parent: BucketFilledState) -> str:
    return f'{_name(parent)} -> {_name(state)} [label="{_link_label(action)}"]'


def to_dot(graph: Graph) -> str:
    """Converts a bucket graph into a DOT graph"""

    return f"""
digraph steps {{
    {r'''
    '''.join(_state_row(state) for state in graph.keys())}
    {r'''
    '''.join(_link_row(state, *value) for state, value in graph.items() if value)}
}}"""
