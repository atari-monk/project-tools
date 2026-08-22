### Set up venv + install pytest

```bash
# 1. Create virtual environment
python3 -m venv .venv

# 2. Activate it
source .venv/bin/activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install pytest
python -m pip install pytest

# 5. Verify installation
python -m pytest --version
```

**Note:** In VS Code, select `.venv/bin/python` via **Python: Select Interpreter**.
