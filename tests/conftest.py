import pytest


def pytest_addoption(parser):
    parser.addoption("--excel", action="store", help="Path to the Excel file")
