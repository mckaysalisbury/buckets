import decimal
from typing import Tuple

BucketValueType = decimal.Decimal  # float is cleaner in the test classes for mypy, but doesn't give as good of results
BucketFilledState = Tuple[BucketValueType, BucketValueType]
