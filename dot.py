from type_aliases import BucketFilledState, BucketValueType, Graph

from action import Action


def _name(state: BucketFilledState) -> str:
    return f'l{state[0]}r{state[1]}'


def _label(state: BucketFilledState) -> str:
    return f'({state[0]}, {state[1]})'


def _state_row(state: BucketFilledState) -> str:
    return f'{_name(state)} [label="{_label(state)}"]'


def _link_row(state: BucketFilledState, action: Action, parent: BucketFilledState) -> str:
    return f'{_name(parent)} -> {_name(state)}'


def to_dot(graph: Graph) -> str: 
    basis_case = (BucketValueType(0), BucketValueType(0))

    return f"""
digraph steps {{
    {r'''
    '''.join(_state_row(state) for state in graph.keys())}
    {r'''
    '''.join(_link_row(state, *value) for state, value in graph.items() if value)}
}}"""

