import decimal
from typing import Tuple

# BucketValueType = float # float is cleaner in the test classes for mypy
BucketValueType = decimal.Decimal  # but doesn't give as good of results
BucketFilledState = Tuple[BucketValueType, BucketValueType]
