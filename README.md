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
git clone <your-repo-url>
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

1. Write requirements
2. Write tests (RED phase)
3. Implement code (GREEN phase)
4. Refactor (REFACTOR phase)
5. Measure coverage
6. Review and iterate

## Learning Outcomes Addressed

- LO1: Requirements analysis and testing strategies
- LO2: Test plan design and code instrumentation
- LO3: Testing techniques and coverage analysis
- LO4: Statistical evaluation of testing limitations
- LO5: Code reviews and automated testing (CI/CD)

## Author

Adnan Mahmud