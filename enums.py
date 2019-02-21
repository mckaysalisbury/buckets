from enum import Enum

class BaseAction(Enum):
    Fill = 1
    Empty = 2
    Transfer = 3  # This is a transfer to full


class Target(Enum):
    Left = 1
    Right = 2

    def other(self) -> Enum:
        return Target(Target.Right if self == Target.Left else self.Left)
