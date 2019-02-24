import decimal
from typing import Tuple, Dict, Optional
from action import Action

BucketValueType = decimal.Decimal
BucketFilledState = Tuple[BucketValueType, BucketValueType]
Graph = Dict[BucketFilledState, Optional[Tuple[Action, BucketFilledState]]]