"""The Type aliases used to help mypy type annotations be a lot cleaner"""
import decimal
from typing import Tuple, Dict, Optional
from action import Action

# pylint: disable=invalid-name  # These are constants, sure, but they're really type aliases.

BucketValueType = decimal.Decimal
BucketFilledState = Tuple[BucketValueType, BucketValueType]
Graph = Dict[BucketFilledState, Optional[Tuple[Action, BucketFilledState]]]
