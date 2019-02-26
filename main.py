"""The main function. In charge of the Console UI / IO"""
from argparse import ArgumentParser, ArgumentTypeError
import decimal
import sys

import dot
import solver
from type_aliases import BucketValueType


def _bucket_value_parser(arg: str) -> BucketValueType:
    try:
        return BucketValueType(arg)
    except (ValueError, decimal.InvalidOperation):  # support both conversion errors
        raise ArgumentTypeError("must be a number")


def _non_negative_bucket_value_parser(arg: str) -> BucketValueType:
    value = _bucket_value_parser(arg)
    if value < 0:
        raise ArgumentTypeError("must not be negative")
    return value


def main() -> int:
    """The main console application, as a testable function"""

    parser = ArgumentParser()
    parser.add_argument('left', type=_non_negative_bucket_value_parser)
    parser.add_argument('right', type=_non_negative_bucket_value_parser)
    parser.add_argument('target', nargs='?', type=_bucket_value_parser, default=-1)
    parser.add_argument('--graph', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    if args.graph:
        graph = solver.generate_graph(args.left, args.right)
        result = dot.to_dot(graph, args.target)
        print(result)
        return 0  # success

    try:
        actions, location = solver.solve(
            args.left, args.right, args.target, include_back_edges=args.verbose)

        print("Steps:")
        for index, (action, state) in enumerate(actions):
            print(f"{index + 1}. {action} (bucket state will be {state[0]}, {state[1]})")
        print(f"The target amount will be in the {location.name} bucket")
    except solver.UnsolvableError as ex:
        print("No Solution")
        print(f"Perhaps try one of these:", *sorted(ex.valid))

    return 0  # 0 is success code for command line


if __name__ == '__main__':
    sys.exit(main())
