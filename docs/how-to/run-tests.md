### Run tests

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Install the project in editable mode
python -m pip install -e .

# 3. Run all tests and stop at the first failure
python -m pytest -x
```

**Note:** `-x` stops pytest after the first failed test. If all tests pass, pytest runs the entire test suite.
