"""Self-tests for longest_increasing_run (Q10).

Run with:  python test_longest_increasing_run.py
"""

from longest_increasing_run import longest_increasing_run


CASES = [
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [4]),
    # Runs must be contiguous: [2, 3, 4] here is not adjacent in the input.
    ([1, 2, 3, 2, 3, 4], [1, 2, 3]),
    # Tie in length: the earlier run must win.
    ([1, 2, 9, 3, 4], [1, 2, 9]),
    ([1, 2, 8, 9], [1, 2, 8, 9]),
    # Another tie: both runs have length 2, so the first one wins.
    ([1, 2, 0, 1], [1, 2]),
    ([1, 2, 3, 0, 1, 2], [1, 2, 3]),
    # Equal neighbours are not strictly increasing.
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3, 4], [2, 3, 4]),
    ([-3, -2, -1, -5, 0], [-3, -2, -1]),
    ([0, 0, 0], [0]),
    ([7, 8, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 4, 5, 1, 2, 3], [3, 4, 5]),
]


def main():
    failures = 0
    for numbers, expected in CASES:
        snapshot = list(numbers)
        got = longest_increasing_run(numbers)
        ok = got == expected
        unchanged = numbers == snapshot
        if not ok or not unchanged:
            failures += 1
        print(
            "{} input={!r} -> {!r} (expected {!r}){}".format(
                "PASS" if ok and unchanged else "FAIL",
                snapshot,
                got,
                expected,
                "" if unchanged else "  [INPUT WAS MODIFIED]",
            )
        )
    print("\n{}/{} cases passed".format(len(CASES) - failures, len(CASES)))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
