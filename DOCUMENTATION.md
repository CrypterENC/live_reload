# auto_live_reload Documentation

## Overview
`auto_live_reload` is a Python library that monitors your project files for changes and automatically restarts your script. It is ideal for CLI tools, scripts, and small services where rapid development and feedback are needed.

## Installation
Install from PyPI:
```bash
pip install auto_live_reload
```
Or for local development:
```bash
pip install -e .
```

## Basic Usage
Add `from auto_live_reload import LiveReload, start_auto_live_reload` at the start of your main script:
```python
from auto_live_reload import LiveReload, start_auto_live_reload

start_auto_live_reload()

def main():
    print("Running business logic…")
    # ...

if __name__ == "__main__":
    main()
```
Any changes to watched files will restart your script automatically.

## Configuration Options
You can customize the behavior using arguments:
```python
start_auto_live_reload(
    patterns=["*.py", "*.jinja"],
    delay=1,
)
```
- `patterns`: List of file patterns to watch (default: `['*.py']`).
- `delay`: Initial delay before watching starts (default: 2).

## Command-Line Usage
You can run the watcher from the command line:
```bash
python -c "import auto_live_reload; auto_live_reload.main()" --interval 2 --patterns "*.py" "*.md"
```
CLI flags:
- `--patterns` PATTERN [PATTERN ...]
- `--exclude` PATTERN [PATTERN ...]
- `--interval` SECONDS
- `--delay` SECONDS
- `--no-recursive`
- `--verbose`

## Development Workflow
1. Clone the repository.
2. Install in editable mode: `pip install -e .`
3. Add `start_auto_live_reload()` to your script.
4. Make code changes and see automatic restarts.

## Issues & Contributions
Issues and pull requests are welcome!
