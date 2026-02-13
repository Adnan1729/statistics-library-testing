# Statistics Library - TDD Project

A Python statistics library built using Test-Driven Development (TDD) methodology.

## Purpose

This project demonstrates comprehensive software testing practices including:
- Test-Driven Development
- Unit, integration, and performance testing
- Code coverage analysis
- Mutation testing
- Continuous Integration/Continuous Deployment (CI/CD)

## Installation

### Development Setup
```bash
# Clone the repository
git clone https://github.com/Adnan1729/statistics-library-testing
cd statistics-library-testing

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

## Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/statlib --cov-report=html

# Run specific test categories
pytest -m unit
pytest -m integration
pytest -m performance
```

## Project Structure
```
statistics-library-testing/
├── src/statlib/          # Main library code
├── tests/                # Test suite
├── docs/                 # Documentation and reports
└── portfolio/            # Portfolio submission
```

## Development Workflow

Write requirements -> Write tests (RED phase) -> Implement code (GREEN phase) -> Refactor (REFACTOR phase) -> Measure coverage -> Review and iterate -> (Write requirements...iterate back)

## Learning Outcomes Addressed

- LO1: Requirements analysis and testing strategies
- LO2: Test plan design and code instrumentation
- LO3: Testing techniques and coverage analysis
- LO4: Statistical evaluation of testing limitations
- LO5: Code reviews and automated testing (CI/CD)

## Author

Adnan Mahmud
