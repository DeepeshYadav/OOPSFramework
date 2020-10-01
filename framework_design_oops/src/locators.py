from selenium.webdriver.common.by import By
from framework_design_oops.testdata.constant import *
from framework_design_oops.testdata.test_data_file import check_in_date, check_out_date

X = By.XPATH
N = By.NAME
C = By.CSS_SELECTOR
I = By.ID
LINKTEXT = By.LINK_TEXT


GOOGLE_SEARCH_BOX = (By.NAME, "q")
GOOGLE_SEARCH_BUTTON = (By.NAME, "btnK")

# Goibibo Go website locators Hotel Booking
HOTELS_ICON = (X, "//a[@href='/hotels/']//span[text()='Hotels']")
INDIA_HOTEL_RADIO_LABEL = (X, "(//input[@name='CountryType'])[1]")
INTER_HOTEL_RADIO_LABEL = (X, "(//input[@name='CountryType'])[2]")
HOTEL_LANDMARK = (I, "downshift-1-input")
HOTE_PAGE_HEADER_ELEMENT = (X, f"//h1[contains(text(), '{HOTEL_PAGE_HEADER}')]")
HOTEL_LOCATION_DROP_DOWN = (I, "downshift-1-menu")
LOCATION_LIST = (X, "//ul[@id='downshift-1-menu']//li")

CHECKIN_CALENDER = (X, "//div[@data-testid='openCheckinCalendar']")
CHECKIN_DATE_ELEMENT = (X, f"//span[text()='{check_in_date}']")
CHECKOUT_DATE_ELEMENT = (X, f"//span[text()='{check_out_date}']")

GUEST_AND_ROOM_ELEM = (X, "//input[@value='2 Guests in 1 Room ']")

EXISTING_ROOM_ELEM = (X, "(//input[@value='2 Guests in 1 Room ']//parent::div//h4)[1]")
EXISTING_ADULT_ELEM = (X, "(//input[@value='2 Guests in 1 Room ']//parent::div//h4)[2]")
EXISTING_CHILD_ELEM = (X, "(//input[@value='2 Guests in 1 Room ']//parent::div//h4)[3]")

ADD_ROOM_ELEM = (X, "(//span[text()='+'])[1]")
ADD_ADULT_ELEM = (X, "(//span[text()='+'])[2]")
ADD_CHILD_ELEM = (X, "(//span[text()='+'])[3]")
DONE_BUTTON = (X, "//button[text()='Done']")
SEARCH_BUTTON = (X, "//button[@data-testid='searchHotelBtn']")


# Cab Booking Options

CAB_BOOKING_ICON = (X, "//span[contains(text(), 'Cabs') and contains(@class, 'iconText ')]")
CAB_SOURCE_ELEMENT = (X, "//p[@data-testid='srcName']")
CAB_DEST_ELEMENT = (X, "//p[@data-testid='destCityName']")
CAB_INPUT_CITY_ELEMENT = (I, "gosuggest_inputL")
CAB_DROP_DOWN_SECTION = (X, "//section[@class='searchCustomBlk']//div//*")
CAB_DATE_CALENDER = (X, "//div[@class='DayPickerInput']")
CAB_BOOKING_DATES = (X, "//div[@class='DayPickerInput']//div//*")
CAB_BOOKING_SEARCH = (X, "//button[@class='searchBtn']")



