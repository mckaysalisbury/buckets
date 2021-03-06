"""This does the heavy lifting in solving the problem, but isn't in charge of IO"""

import collections
from typing import Callable, List, Optional, Tuple, Deque, Set

from performer import get_performer
from action import Action
from enums import BaseAction, Target
from type_aliases import BucketFilledState, BucketValueType, Graph


class UnsolvableError(Exception):
    """Determined to be unsolvable. Makes a `valid` value available with the valid values"""
    def __init__(self, valid: Set[BucketValueType]):
        super().__init__()
        self.valid = valid


ALL_ACTIONS = [Action(action, target) for action in BaseAction for target in Target]


def solve(
        max_left: BucketValueType, max_right: BucketValueType,
        target_amount: Optional[BucketValueType] = BucketValueType(-1)
    ) -> Tuple[List[Tuple[Action, BucketFilledState]], Target]:
    """Returns the list of actions, and a bucket which contains the correct amount"""

    # Variables which save the state for later calling
    found_state: Optional[BucketFilledState] = None
    direction: Optional[Target] = None

    def break_out_early(current: BucketFilledState) -> bool:
        """returns the target if it's found, otherwise None"""
        nonlocal found_state, direction
        if current[0] == target_amount:
            found_state = current
            direction = Target.Left
            return True
        if current[1] == target_amount:
            found_state = current
            direction = Target.Right
            return True
        return False

    graph = generate_graph(max_left, max_right, break_out_early)

    if found_state and direction:
        current_bucket_state = found_state
        path: List[Tuple[Action, BucketFilledState]] = []
        while True:
            node = graph[current_bucket_state]
            if node is None:
                return path, direction
            action, next_bucket_state = node
            path.insert(0, (action, current_bucket_state))
            current_bucket_state = next_bucket_state

    # couldn't find a solution, exhaustively find all results
    valid = set(values for left, right in graph for values in [left, right])
    raise UnsolvableError(valid)


def generate_graph(
        max_left: BucketValueType, max_right: BucketValueType,
        break_out_early: Callable[[BucketFilledState], bool] = lambda _: False) -> Graph:
    """Generates a whole graph"""

    # A queue allows us to do a breadth-first traversal, which will guarantee "optimal" solutions
    actions_to_consider: Deque[Tuple[Action, BucketFilledState]] = collections.deque()
    graph: Graph = {}

    def put_all(current: BucketFilledState) -> None:
        for action in ALL_ACTIONS:
            actions_to_consider.appendleft((action, current))

    perform = get_performer(max_left, max_right)

    basis_case = (BucketValueType(0), BucketValueType(0))

    graph[basis_case] = None  # Base case
    if break_out_early(basis_case):
        return graph

    put_all(basis_case)  # Starting condition is both are empty

    while actions_to_consider:
        action_considering, parent = actions_to_consider.pop()
        result_of_action = perform(action_considering, parent)

        if result_of_action not in graph:
            graph[result_of_action] = (action_considering, parent)

            if break_out_early(result_of_action):
                return graph

            put_all(result_of_action)

    return graph
