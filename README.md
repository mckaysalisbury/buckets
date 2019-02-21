
Usage
---

I used Python 3. The code can run on python 2, with backports. Exercise left to the reader.

    python main.py LEFT_BUCKET_SIZE RIGHT_BUCKET_SIZE TARGET_SIZE

Setup (only needed for tests)
---

    pip -r requirements.txt

Running Tests
---

    pytest

    mypy main.py solver.py performer.py enums.py --strict

Todo
---

* I don't have tests for the main method, but that gets manually tested when I run it. Maybe I'll do this later.
* I'd like to clean up the mypy for `decimal` type, but `int` and `float` are clean for mypy, and I want to get to sleep.
* There's probably some logic involving GCD to make impossible target sizes detect easier, but that's not part of the requirements, and doing it this way, we get some fun information
* I really want to output a DOT graph for visualization, but that'll have to wait for another day.
