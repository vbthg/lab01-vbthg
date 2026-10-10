# Study Assistant - Lab 1

A small rule-based study assistant for CSC10014. It answers greetings and looks
up campus office locations and opening hours from `data/offices.csv`.
Lab 1 adds the greeting `good morning`; this app does not use an LLM or API key.

## Prerequisites

- Python 3.10 or newer (tested with Python 3.12.4).
- Git, with your own commit name and email configured.
- Internet access to clone the repository and install packages.
- Optional: VS Code with the Microsoft Python and Pylance extensions.

Check `python --version` and `git --version`. On Windows, use `py` instead of
`python` when creating the environment if `python` is unavailable.
If needed, configure Git with your own details:

```text
git config --global user.name "Your name"
git config --global user.email "your-email@example.com"
```

## Setup

Clone the project and enter its root folder:

```text
git clone https://github.com/vbthg/lab01-vbthg.git
cd lab01-vbthg
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

On Windows Git Bash, activate with `source .venv/Scripts/activate`.
Keep the virtual environment active when running commands below. In VS Code,
open the whole folder and select `.venv` via **Python: Select Interpreter**.
The packages are installed into `.venv`; do not commit this folder.

## Run

Run from the repository root:

```text
python -m assistant "where is the training office?"
```

Expected output:

```text
Training Office: room I.101, open Mon-Fri 07:30-16:30.
```

Try the Lab 1 improvement:

```text
python -m assistant "Good morning!"
```

Expected output: `Hello! Ask me where an office is, or when it opens.`

For interactive mode, run `python -m assistant`, type a message, then type
`quit` or `exit` to leave. The office data file must remain in `data/`.

## Test and environment check

```text
python -m pytest -q
python scripts/check_env.py
```

Expected: **8 passed** (the elapsed time varies), then every environment check
shows `[ OK ]` and the final line is `All good!`.
Run `git status --ignored` to confirm `.venv/` is ignored.

## Project structure

| Path | Purpose |
| --- | --- |
| `src/assistant/` | Assistant rules and command-line entry point |
| `tests/` | Greeting, office lookup and basic response tests |
| `data/` | Small sample office data in CSV format |
| `docs/` | Project documentation and Lab 1 verification records |
| `ui/` | Placeholder for the future user interface |
| `scripts/check_env.py` | Development environment checks |
| `requirements.txt` | Direct dependency pinned to an exact version |
| `pyproject.toml` | Package metadata and pytest configuration |
| `.gitignore` | Excludes local environments, caches and secrets |

## Troubleshooting

- **Python not found on Windows:** use `py`, or install Python with Add to PATH.
- **PowerShell blocks activation:** use `.\.venv\Scripts\python.exe` instead of
  `python` for each install, run, test and check command. Activation is optional
  when calling this interpreter explicitly. Alternatively, use Git Bash.
- **No module named assistant / pytest:** check the selected Python with
  `python -c "import sys; print(sys.executable)"`, activate `.venv`, and repeat
  the two installation commands.
- **No module named venv on Ubuntu:** install `python3-venv` before setup.
- **Permission error in the temporary directory during setup:** this occurred
  in the automated setup session. Use a writable temporary directory for that
  terminal session, then retry:

  ```powershell
  New-Item -ItemType Directory -Force .setup-temp | Out-Null
  $env:TEMP = (Resolve-Path .setup-temp).Path
  $env:TMP = $env:TEMP
  py -m venv .venv
  ```

- **CSV not found:** keep `data/offices.csv` next to `src/` in the repository.
- **Environment check reports missing Git email:** configure your own Git email
  using the command in Prerequisites.

## Pair verification

A partner from another team should clone into a fresh folder and follow only
this README. The target is passing tests within 10 minutes. Store their completed
verification sheet in `docs/lab1/pair_verification.md` after the real check.

AI assistance is disclosed in `docs/ai-use-log.md`. Read and understand the
changes before submitting them.
