# run_tests.py
"""
Runner file for the automated testing suite. Uses pytest-html command to generate a html testing report.
"""
import subprocess

if __name__ == "__main__":
    # pytest-html command call
    subprocess.call("python -m pytest --html=report.html --self-contained-html")
