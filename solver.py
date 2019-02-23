import collections
from typing import Dict, List, Optional, Tuple, Deque, Set

from performer import get_performer
from action import Action
from enums import BaseAction, Target
from type_aliases import BucketFilledState, BucketValueType


class UnsolvableError(Exception):
    """Determined to be unsolvable. Makes a `valid` value available with the valid values"""
    def __init__(self, valid: Set[BucketValueType]):
        self.valid = valid


all_actions = [Action(action, target) for action in BaseAction for target in Target]


def solve(max_left: BucketValueType, max_right: BucketValueType, target_amount: BucketValueType) -> Tuple[List[Tuple[Action, BucketFilledState]], Target]:
    """Returns the list of actions, and a bucket which contains the correct amount"""
    actions_to_consider : Deque[Tuple[Action, BucketFilledState]] = collections.deque()  # for breadth first traversal
    graph: Dict[BucketFilledState, Optional[Tuple[Action, BucketFilledState]]] = {}

    def put_all(current: BucketFilledState) -> None:
        for action in all_actions:
            actions_to_consider.appendleft((action, current))

    perform = get_performer(max_left, max_right)

    
    def done(current: BucketFilledState) -> Optional[Target]:
        """returns the target if it's found, otherwise None"""
        if current[0] == target_amount:
            return Target.Left
        elif current[1] == target_amount:
            return Target.Right
        else:
            return None

    basis_case = (BucketValueType(0), BucketValueType(0))

    found = done(basis_case)
    if found:
        return [], found

    put_all(basis_case)  # Starting condition is both are empty
    graph[basis_case] = None  # Base case

    while len(actions_to_consider) > 0:
        action_considering, parent = actions_to_consider.pop()
        result_of_action = perform(action_considering, parent)

        if result_of_action not in graph:
            graph[result_of_action] = (action_considering, parent)            

            # break out early if you found a solution
            found = done(result_of_action)
            if found:
                current_bucket_state = result_of_action
                path: List[Tuple[Action, BucketFilledState]] = []
                while True:
                    node = graph[current_bucket_state]
                    if node is None:
                        return path, found
                    action, next_bucket_state = node
                    path.insert(0, (action, current_bucket_state))
                    current_bucket_state = next_bucket_state

            put_all(result_of_action)

    # couldn't find a solution, exhaustively
    valid = set(values for left, right in graph.keys() for values in [left, right])
    raise UnsolvableError(valid)
