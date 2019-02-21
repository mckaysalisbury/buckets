from enums import BaseAction, Target
from typing import Callable, Tuple
from action import Action

from type_aliases import BucketFilledState, BucketValueType


def get_performer(max_left: BucketValueType, max_right: BucketValueType) -> Callable[[Action, BucketFilledState], BucketFilledState]:
    def perform(action: Action, input: BucketFilledState) -> BucketFilledState:
        # I don't want to duplicate logic so:
        # Let's assume left
        max_fill = max_left
        # But if not, make adjustments
        if action.target == Target.Right:
            input = input[::-1]
            max_fill = max_right
        # which we'll reverse later
        
        transfer_would_overflow = (input[0] + input[1] > max_fill)
        typed_zero = BucketValueType(0)
        actions_performed = {
            BaseAction.Fill: (max_fill, input[1]),
            BaseAction.Empty: (typed_zero, input[1]),
            BaseAction.Transfer: (
                max_fill if transfer_would_overflow else input[0] + input[1],
                input[1] - (max_fill - input[0]) if transfer_would_overflow else typed_zero
            )
        }
        output = actions_performed[action.base]

        # Fix if necessary
        if action.target == Target.Right:
            output = output[::-1]
        
        return output
    return perform
