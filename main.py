import decimal
import sys
from typing import List

import solver
from type_aliases import BucketValueType

def usage() -> int:
    print("USAGE: python solver.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE [TARGET_SIZE]")
    return 1
    

def main(*args: str) -> int:

    if len(args) == 3:
        try:
            args_to_pass = [BucketValueType(arg) for arg in args]
        except (ValueError, decimal.InvalidOperation):  # decimal throws a different conversion error than int and float
            print("Arguments must be numbers")
            return usage()

        try:
            actions, location = solver.solve(*args_to_pass)

            print("Steps:")            
            for index, action in enumerate(actions):
                print(f"{index + 1}. {action}")
            print(f"The target amount will be in the {location.name} bucket")
        except solver.UnsolvableError as ex:
            print("No Solution")
            print(f"Perhaps try one of: {ex.valid}")
            # return 1  # I'm tempted to say this might be a failure case, but this is part of its job, which it did successfully
    else:
        print("Incorrect number of arguments")
        return usage()

    return 0  # 0 is success code for command line


if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    sys.exit(main(*args))
