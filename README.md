# Student Information System

A beginner-friendly Python project demonstrating professional project structure, configuration with environment variables, JSON data loading, validation, grade calculation, logging, reports, automated tests, and Git workflow.

## Features
- Loads app configuration from `.env` using `python-dotenv`
- Reads student records from `data/student.json`
- Validates names and marks (0–100)
- Calculates grades and student status
- Generates a readable student report
- Handles invalid input and logs application events
- Includes pytest tests for calculator and validation modules

## Project structure
```text
student_project/
├── src/student_app/
│   ├── main.py
│   ├── config.py
│   ├── logger.py
│   ├── models/student.py
│   ├── services/calculator.py
│   ├── utils/validation.py
│   └── reports/student_report.py
├── tests/
├── data/student.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
$env:PYTHONPATH = "src"
python -m student_app.main
pytest
```

## Setup (Linux/macOS)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
export PYTHONPATH=src
python -m student_app.main
pytest
```

Never commit `.env`, API keys, or `.venv`. `.env.example` contains placeholders only.
