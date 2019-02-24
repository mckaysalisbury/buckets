
Usage
---

I used Python 3, no requirements. The code can run on python 2, with backports. Exercise left to the reader.

    python main.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE [TARGET_SIZE]

Setup (only needed for tests)
---

    pip -r requirements.txt

Running Tests
---

    pytest

    mypy main.py solver.py performer.py enums.py --strict

Todo
---

* I really want to output a DOT graph for visualization, but that'll have to wait for another day.
* I also want to fully roll up the solving loop, as there's a teeny amount of duplication in setup, but again, sleep.
* There's probably some logic involving GCD to make impossible target sizes detect easier, but that's not part of the requirements, and doing it this way, we get some helpful information to the user.
