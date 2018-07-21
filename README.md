# reading-quantified-py

Python code for analyzing my reading habits. See [reading-quantified](https://github.com/drejkim/reading-quantified) for the web app code.

## Setting up the project

This project uses Python 3, which comes with a built-in module (`venv`) to create virtual environments.

Create the virtual environment:

```bash
python3 -m venv .venv
```

Install the required packages:

```bash
.venv/bin/pip install -r requirements.txt
```

## Creating config.py

Create `config.py` with the following variables:

```
TRELLO_API_KEY = ''
PARSE_APP_ID = ''
PARSE_API_KEY = ''
PARSE_USERNAME = ''
PARSE_PASSWORD = ''
```

## Usage 

```bash
.venv/bin/python books.py
```
