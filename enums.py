"""Enums for the project"""

from enum import Enum

class BaseAction(Enum):
    """Base actions for an action, the three supported actions"""
    Fill = 1
    Empty = 2
    Transfer = 3  # This is a transfer to full


class Target(Enum):
    """The target bucket to perform the action on"""
    Left = 1
    Right = 2

    def other(self) -> Enum:
        """The other bucket, i.e. left, if you're currently right"""
        return Target(Target.Right if self == Target.Left else self.Left)
