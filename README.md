
# Usage

I used Python 3, no requirements. The code could be run on python 2, with backports, but the type annotations would have to be removed. Exercise left to the reader.

    python main.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE [TARGET_SIZE] [--graph]

## Examples

    python main.py 7 5 3  # solves for 3 in buckets of sizes 7 and 5
    python main.py 7 5  # gives a list of all of the solutions for buckets of 7 and 5
    python main.py 7 5 --graph | dot -Tpng > 75.png  # creates a graph of the solution tree for buckets of size 7 and 5 (requires graphviz to be installed)

# Setup (only needed for tests)

    pip -r requirements.txt

# Running Tests

    pytest

    mypy main.py solver.py performer.py enums.py --strict

# Todo

* Label the edges of the graph with the action to take to get there
* Highlight the target option(s) for graph visualization
* I also want to fully roll up the solving loop, as there's a teeny amount of duplication in setup, but again, sleep.
* There's probably some logic involving GCD to make impossible target sizes detect easier, but that's not part of the requirements, and doing it this way, we get some helpful information to the user.
