"""Performs the actions on bucket states"""

from typing import Callable

from action import Action
from enums import BaseAction, Target
from type_aliases import BucketFilledState, BucketValueType


def get_performer(
        max_left: BucketValueType, max_right: BucketValueType
    ) -> Callable[[Action, BucketFilledState], BucketFilledState]:
    """Gets a performer based on the specified bucket sizes"""
    def perform(action: Action, initial_state: BucketFilledState) -> BucketFilledState:
        """Performs the action on the specified bucket state (with the closed over bucket sizes)"""
        # I don't want to duplicate logic so:
        # Let's assume left
        max_fill = max_left
        # But if not, make adjustments
        if action.target == Target.Right:
            initial_state = initial_state[::-1]
            max_fill = max_right
        # which we'll reverse later

        transfer_would_overflow = (initial_state[0] + initial_state[1] > max_fill)
        typed_zero = BucketValueType(0)
        actions_performed = {
            BaseAction.Fill: (max_fill, initial_state[1]),
            BaseAction.Empty: (typed_zero, initial_state[1]),
            BaseAction.Transfer: (
                max_fill
                if transfer_would_overflow else initial_state[0] + initial_state[1],
                initial_state[1] - (max_fill - initial_state[0])
                if transfer_would_overflow else typed_zero
            )
        }
        final_state = actions_performed[action.base]

        # Fix if necessary
        if action.target == Target.Right:
            final_state = final_state[::-1]

        return final_state
    return perform
