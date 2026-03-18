# Beams & Brackets Safety Validator

## Objective
Build a CI/CD pipeline for a CLI tool that validates safety compliance checklists for ADU construction sites. Every update should be automatically testes, linted, and packaged into a Docker image to prevent faulty safety protocols.

## Requirements

1. CLI Utility
    - Language: Python
    - Input: JSON file containing safety checks (e.g., **Hard hats present**, **Scaffolding inspected**)
    - Output: **Pass** if all required fields are populated, **Fail** otherwise
    - Must handle missing or incomplete data

2. Automated Testing
    - Include at least 3 unit tests
    - Verify behavior for complete data and missing data scenarios

3. CI/CD Pipeline (Github Actions)
    - Trigger: On every push to the main branch
    - Stages:
        1. Code linting using Flake8
        2. Unit tests using pytest
        3. Build Docker image for production-ready CLI
    - Must provide immediate feedback on code quality and functional integrity

4. Containerization
    - Dockerfile to package the CLI tool and its dependencies
    - Resulting image should be production-ready

5. Documentation
    - README.md describing:
        - How to run the CLI
        - How to run tests
        - How to trigger the pipeline
        - How to view build artifacts

---

## Deliverables
1. A ZIP file containing the complete codebase, including the CLI tool, tests, Dockerfile, and .github/workflows folder.
2. A link to a public GitHub repository where the pipeline is actively running.
3. Screenshots of a successful GitHub Actions run showing all stages (Lint, Test, Build) passing.
4. A text file containing the output logs of a successful Docker build command executed locally.