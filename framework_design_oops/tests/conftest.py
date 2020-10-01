import pytest
from framework_design_oops.src.app_logic import AppFunction
from framework_design_oops.testdata.test_data_file import *

"""
default scope of fixture is function level.
scope="function"  : Execute fixture before each test function execution.
scope="module"  " : Execute fixture for entire module
scope="session"  : Execute fixture for entire automation for all different test function files.
"""


@pytest.fixture(scope="module")
def setup():
    obj = AppFunction(browser, url, wait_time)
    return obj