import sys

import solver
from type_aliases import BucketValueType

def usage() -> None:
    print("USAGE: python solver.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE [TARGET_SIZE]")
    exit(1)
    

def main() -> None:
    args = sys.argv
    args.pop(0)    

    if len(args) == 3:
        try:
            args_to_pass = [BucketValueType(arg) for arg in args]
        except ValueError:
            print("Arguments must be numbers")
            usage()

        try:
            actions, location = solver.solve(*args_to_pass)

            print("Steps:")            
            for index, action in enumerate(actions):
                print(f"{index + 1}. {action}")
            print(f"The target amount will be in the {location.name} bucket")
        except solver.UnsolvableError as ex:
            print("No Solution")
            print(f"Perhaps try one of: {ex.valid}")
    else:
        print("Incorrect number of arguments")
        usage()


if __name__ == '__main__':
    main()
