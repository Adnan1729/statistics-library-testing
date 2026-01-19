"""
Setup configuration for statistics library.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="statlib-tdd",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A statistics library built with Test-Driven Development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/statistics-library-testing",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "pytest-benchmark>=4.0.0",
            "hypothesis>=6.98.0",
            "black>=24.1.1",
            "pylint>=3.0.3",
            "mypy>=1.8.0",
        ],
    },
)