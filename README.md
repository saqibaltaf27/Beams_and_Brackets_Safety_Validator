# Beams & Brackets Safety Validator

## Overview
The **Beams & Brackets Safety Validator** is a CLI tool designed to validate safety compliance checklists for ADU (Accessory Dwelling Unit) construction sites.
It ensures all required safety protocols are checked before issuing checklists to foremen, preventing faulty safety procedures from reaching the job site.

The project includes a **fully automated CI/CD pipeline** that lints code, runs tests, and build a Docker image.

---

## Features

- Validate JSOn safety checklists and return **Pass/Fail**
- Handles **missing fields** and **invalid JSON**
- Automated CI/CD pipeline:
    - **Linting** using Flake8
    - **Unit tests** using pytest
    - **Docker image build** for production-ready CLI

---

## Installation & Setup

1. Clone the repository
git clone https://github.com/saqibaltaf27/Beams_and_Brackets_Safety_Validator.git

cd Beams_and_Brackets_Safety_Validator

2. Create a Virtual Environment
python -m venv venv

3. Activate Virtual Environment
venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

---

## CLI USAGE
Prepare a JSON file like safety_check.json:

```JSON
{
    "Hard hats present": true,
    "Scaffolding inspected": true,
    "Guard rails installed": true,
    "Electrical hazards addressed": true
}
```

Run the CLI: python -m cli.main safety_check.json
Result: Pass

Error Handling:

```JSON

{
    "Hard hats present": true,
    "Scaffolding inspected": true,
    "Guard rails installed": true,
    
}

```

Result: 
```Bash
(venv) PS C:\POSTWORK\Beams_and_Brackets_Safety_Validator> python -m cli.main safety_check.json
Fail: 'Electrical hazards addressed' missing or not True.
(venv) PS C:\POSTWORK\Beams_and_Brackets_Safety_Validator> 

```

## Running Tests
Unit tests verify the CLI handles complete, incomplete, and invalid JSOn data.

```bash
python -m pytest tests
```

Result:
```bash
(venv) PS C:\POSTWORK\Beams_and_Brackets_Safety_Validator> python -m pytest tests
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.8.0, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\POSTWORK\Beams_and_Brackets_Safety_Validator
collected 3 items                                                                                                                                           

tests\test_validator.py ...                                                                                                                           [100%]

==================================================================== 3 passed in 0.03s =====================================================================
(venv) PS C:\POSTWORK\Beams_and_Brackets_Safety_Validator>

```
It Run 3 unit tests and reports success.

---

## Linting
Check code quality using Flake8:
```bash
python -m flake8 cli tests
```

---

## Docker Instructions
Build Docker Image

```bash

docker build -t beams-brackets-safety-validator:latest .

```

Run Docker Container
docker run --rm -v ${PWD}\safety_check.json:/app/safety_check.json beams-brackets-safety-validator:latest /app/safety_check.json

---

## CI/CD Pipeline

The project includes a GitHub Actions workflow located at .github/workflows/ci-cd.yml:

# Pipeline stages:

1. Lint – Ensures code style and quality using Flake8

2. Test – Runs unit tests with pytest

3. Docker Build – Builds a production-ready Docker image

Trigger: On push to main branch

Each stage runs automatically and provides immediate feedback in GitHub Actions

