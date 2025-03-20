from setuptools import setup, find_packages

setup(
    name="portfolio_optimizer",
    version="0.1",
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "numpy",
        "pandas",
        "yfinance",
    ],
    python_requires=">=3.7",
)