
# Python Homework 2 — Bond Pricing, Duration & FizzBuzz (NumPy)

## Instructions

1. Update `WhoAmI_File.py` to return **your UNI** (instead of `'djr2132'`).
2. Implement the functions in each of the following files using **NumPy vectorized code (no loops)**:
   - `BondPrice_File.py` — `getBondPrice(y, face, couponRate, m, ppy=1)`
   - `BondDuration_File.py` — `getBondDuration(y, face, couponRate, m, ppy=1)`
   - `FizzBuzz_File.py` — `FizzBuzz(start, finish)`

**Important:** All functions (except WhoAmI) must use NumPy with vectorized operations. No `for` or `while` loops allowed — the tests will check for this.

## Running Tests Locally

    pip install pytest numpy
    pytest test_UnitTests.py -v

## Autograding

Tests run automatically when you push to this repository. Check the **Actions** tab to see your results.
