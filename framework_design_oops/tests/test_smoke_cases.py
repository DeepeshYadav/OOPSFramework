from framework_design_oops.testdata.test_data_file import *
from framework_design_oops.src.external_function import get_cell_data
import logging
logger = logging.getLogger(__name__)
import  pytest
from time import  sleep



def test_search_on_google(setup):
    try:
        logger.info("test cases: test_search_on_google, executed started")
        setup.search_on_google(search_value)
        setup.close_browser()
        logger.info("test cases: test_search_on_google, executed successfully")
    except Exception as e:
        logging.exception(f"test case : test_search_on_google, execution failed :")
        raise(e)

def test_book_hotel(setup):
    logger.info("test cases: test_book_hotel, executed started")
    setup.navigate_hotel_page()
    setup.type_of_hotel()
    setup.search_hotel_location(HOTEL_LOCATION)
    setup.select_hotel_location(HOTEL_LOCATION)
    setup.select_checkin_and_checkout_date()
    setup.add_room_adult_child(rooms, adults, childs)
    setup.click_on_search_button()
    sleep(10)

def test_cab_booking(setup):
    logger.info("Cab booking feature test case execution started")
    setup.nagivate_to_cab_booking_page()
    setup.select_source_place_for_cab(get_cell_data(1, 2), get_cell_data(2, 2))
    sleep(10)
    setup.select_Date(get_cell_data(3, 2))
    sleep(10)