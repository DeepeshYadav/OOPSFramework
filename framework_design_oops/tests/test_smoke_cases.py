from framework_design_oops.testdata.test_data_file import *

def test_search_on_google(setup):
    setup.search_on_google(search_value)
    setup.close_browser()