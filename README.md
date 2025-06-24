# Advanced CLI Calculator

A modular, extensible command-line calculator built in Python featuring:

- Expression evaluation with multiple operations
- History tracking with undo/redo support (Memento pattern)
- Persistent history saving/loading via CSV files
- Observer pattern to update history automatically
- Robust error handling and input validation
- Configurable via environment variables (.env)
- Full unit test coverage with pytest and GitHub Actions CI

---

## Features

- Evaluate complex arithmetic expressions
- Undo and redo calculation history states
- Save and load calculation history
- Clear history on demand
- Detailed error messages on invalid input
- Easily configurable history file path via environment variables
- Designed with modular code and OOP design patterns (Observer, Memento, Factory)

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/advanced-cli-calculator.git
   cd advanced-cli-calculator

2. Create and activate a virtual environment

    ```bash
    python -m venv venv
    On Windows: venv\Scripts\activate # on mac source venv/bin/activate 

3. Install dependencies

    ```bash
    pip install -r requirements.txt

4. Setup environment variables:

    ```bash
        # creat a .env file in the root directory 
    HISTORY_FILE = history.csv

## Usage

Run the calculator REPL (Read-Eval-Print Loop) from the command line:

```bash
python main.py
 ```

Example session:
```bash
    >>> 2 + 2
    Result: 4
    >>> history
    1: 2 + 2 = 4
    >>> undo
    Undo successful.
    >>> exit
    Goodbye!
```
## Test
```bash 
pytest --cov=app --cov-report= term-missing
