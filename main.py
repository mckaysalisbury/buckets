"""The main function. In charge of the Console UI / IO"""
import decimal
import sys

import dot
import solver
from type_aliases import BucketValueType


def usage(arg: str) -> int:
    """Prints the usage, and returns the error code"""
    print(arg)
    print("USAGE: python solver.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE [TARGET_SIZE] [--graph]")
    return 1  # failure code for command line


def main(*args_tuple: str) -> int:
    """The main console application, as a testable function"""
    args = list(args_tuple)
    graph_option = '--graph'
    requested_graph = graph_option in args
    if requested_graph:
        args.remove(graph_option)

    if len(args) in [2, 3]:
        try:
            args_to_pass = [BucketValueType(arg) for arg in args]
        except (ValueError, decimal.InvalidOperation):  # support both conversion errors
            return usage("Arguments must be numbers")

        if any(arg < 0 for arg in args_to_pass[:2]):  # The first two arguments must not be negative
            return usage("Bucket sizes must be positive")

        if requested_graph:
            target = args_to_pass[2] if len(args_to_pass) > 2 else BucketValueType(-1)
            graph = solver.generate_graph(args_to_pass[0], args_to_pass[1])
            result = dot.to_dot(graph, target)
            print(result)
            return 0  # success

        try:
            actions, location = solver.solve(*args_to_pass)

            print("Steps:")
            for index, (action, state) in enumerate(actions):
                print(f"{index + 1}. {action} (bucket state will be {state[0]}, {state[1]})")
            print(f"The target amount will be in the {location.name} bucket")
        except solver.UnsolvableError as ex:
            print("No Solution")
            print(f"Perhaps try one of these:", *sorted(ex.valid))
    else:
        return usage("Incorrect number of arguments")

    return 0  # 0 is success code for command line


if __name__ == '__main__':
    ARGS = sys.argv
    ARGS.pop(0)
    sys.exit(main(*ARGS))
