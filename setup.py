"""Setup configuration for Titanic Survival Prediction project."""

from setuptools import setup, find_packages

setup(
    name="titanic-survival-prediction",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
    ],
    extras_require={
        "dev": [
            "flake8>=4.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ]
    },
)
