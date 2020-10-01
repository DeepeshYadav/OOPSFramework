from framework_design_oops.browser_actions.browser_actions import BrowserAction
from .locators import *
from datetime import datetime
import  logging

logger = logging.getLogger(__name__)

class AppFunction(BrowserAction):

    def __init__(self, browser, url, wait_time):
        self.url = url
        super().__init__(browser, wait_time)
        self.launch_app()

    def launch_app(self):
        #logger.info("Browser has launched")
        logger.error("There is some issue in browser launching")
        self.spdriver.get(self.url)

    # def close_browser(self):
    #     self.spdriver.close()

    def search_on_google(self, value):
        self.input_text(GOOGLE_SEARCH_BOX, value)
        self.click_element(GOOGLE_SEARCH_BUTTON)

    def navigate_hotel_page(self):
        self.click_element(HOTELS_ICON)
        self.verify_element_is_visible(HOTE_PAGE_HEADER_ELEMENT)
        self.take_screen_shot("hotel")

    def type_of_hotel(self, number=1):
        """
        :param int number: number = 1 then search for Indian hotels, if number = 2 search for international hotels
        :return:
        """
        if number == 1:
            self.click_element(INDIA_HOTEL_RADIO_LABEL)
        elif number == 2:
            self.click_element(INTER_HOTEL_RADIO_LABEL)
        else:
            logger.debug("Please provide appropriate number either it will be 1 or 2")
            raise

    def search_hotel_location(self, location):
        self.click_element(HOTEL_LANDMARK)
        self.input_text(HOTEL_LANDMARK, location)

    def select_hotel_location(self, location):
        locationlist = self.get_all_elements(LOCATION_LIST)
        for city in locationlist:
            print(city.text)
            logger.info(f"location :{city.text}")
            place = (city.text).split("\n")[0]
            if place == location:
                city.click()
                break
            else:
                continue

    def select_checkin_and_checkout_date(self):
        self.click_element(CHECKIN_CALENDER)
        self.click_element(CHECKIN_DATE_ELEMENT)
        self.click_element(CHECKOUT_DATE_ELEMENT)

    def add_room_adult_child(self, room=None, adult=None, child=None):
        self.click_element(GUEST_AND_ROOM_ELEM)
        if room is not None:
            exiting_room = self.get_text_of_element(EXISTING_ROOM_ELEM)
            if int(exiting_room) > room:
                pass
            else:
                for i in range(room-int(exiting_room)):
                    self.click_element(ADD_ROOM_ELEM)
        if adult is not None:
            exiting_adult = self.get_text_of_element(EXISTING_ADULT_ELEM)
            if int(exiting_adult) > adult:
                pass
            else:
                for i in range(adult-int(exiting_adult)):
                    self.click_element(ADD_ADULT_ELEM)

        if child is not None:
            exiting_child = self.get_text_of_element(EXISTING_CHILD_ELEM)
            if int(exiting_child) > child:
                pass
            else:
                for i in range(child-int(exiting_child)):
                    self.click_element(ADD_CHILD_ELEM)
        self.click_element(DONE_BUTTON)


    def click_on_search_button(self):
        self.click_element(SEARCH_BUTTON)

    # CAB BOOKING FEATURE

    def nagivate_to_cab_booking_page(self):
        self.click_element(CAB_BOOKING_ICON)

    def select_source_place_for_cab(self, src_location, dest_location):
        self.click_element(CAB_SOURCE_ELEMENT)
        self.input_text(CAB_INPUT_CITY_ELEMENT, src_location)
        all_element = self.spdriver.find_elements_by_xpath(CAB_DROP_DOWN_SECTION[1])
        for element in all_element:
            src = (element.text).split("\n")[0]
            print(element.tag_name)
            logger.info(element.tag_name)
            if src == src_location:
                element.click()
                break
            else:
                continue

        self.input_text(CAB_INPUT_CITY_ELEMENT, dest_location)
        all_elements = self.spdriver.find_elements_by_xpath("//section[@class='searchCustomBlk']//div//*")
        for elem in all_elements:
            dest = (elem.text).split("\n")[0]
            logger.info(elem.tag_name)
            if dest == dest_location:
                elem.click()
                break
            else:
                continue


    def select_Date(self, traveldate):
        self.click_element(CAB_DATE_CALENDER)
        date_elements = self.get_all_elements(CAB_BOOKING_DATES)
        for elem in date_elements:
            print(elem.text)
            print("Travel date :", traveldate)
            if elem.text == str(traveldate):
                elem.click()
                break
            else:
                continue
        self.click_element(CAB_BOOKING_SEARCH)





