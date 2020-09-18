import pytest
from framework_design_oops.src.app_logic import AppFunction
from framework_design_oops.testdata.test_data_file import *

@pytest.fixture(scope="function")
def setup():
    obj = AppFunction(browser, url, wait_time)
    return obj
