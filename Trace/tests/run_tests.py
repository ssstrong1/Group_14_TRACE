# run_tests.py
"""
Runner file for the automated testing suite. Uses pytest-html command to generate a html testing report.
"""
import subprocess

if __name__ == "__main__":
    """
    Unable to get this file to function properly, just run the command below in the console to run the test suite
    """
    # pytest-html command call
    subprocess.call("python -m pytest -v Trace/tests/ --html=report.html --self-contained-html")
