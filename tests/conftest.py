import pytest

def pytest_addoption(parser):
    """
    Add a command-line option for selecting the browser.
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on. Options: 'chrome', 'firefox', 'edge', 'safari'"
    )
