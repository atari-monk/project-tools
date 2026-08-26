If you want a **one-liner showing your project directory structure** on Ubuntu:

```bash
tree -a -I '.git|node_modules|__pycache__|.venv'
```

If `tree` isn't installed:

```bash
sudo apt install tree -y && tree -a -I '.git|node_modules|__pycache__|.venv'
```

For a **compact structure with only directories + files up to 2 levels deep**:

```bash
find . -maxdepth 2 -not -path './.git*' | sort
```

I’d recommend `tree` for a clean project overview.
