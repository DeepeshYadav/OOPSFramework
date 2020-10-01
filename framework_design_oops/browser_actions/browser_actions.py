from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from framework_design_oops.testdata.test_data_file import *
import logging
import os
from datetime import datetime

#logging.basicConfig(filename=os.path.join(LOG_DIR, "master.log"), level=logging.DEBUG, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
logging.basicConfig(filename=os.path.join(LOG_DIR, "master.log"), level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
#logging.basicConfig(filename=os.path.join(LOG_DIR, "master.log"), level=logging.DEBUG, format=f'%{datetime.time(datetime.now())} %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class BrowserAction():
      def __init__(self, browser, wait_time):
          self.browser = browser
          self.spdriver = None
          self.get_spdriver()
          self.wait = WebDriverWait(self.spdriver, wait_time)

      def click_element(self, selector):
          element = self.wait.until(EC.presence_of_element_located(selector))
          logger.debug(f"This the element on which click action would be performed : {selector}")
          element.click()

      def input_text(self, selector, value):
          logger.debug(f"This the element on which will put new data : {selector}")
          element = self.wait.until(EC.presence_of_element_located(selector))
          element.clear()
          element.send_keys(value)
          logger.info("Click Successfully")

      def verify_element_is_visible(self, selector):
          logger.debug(f" will verify visibility of given element;  {selector} ")
          self.wait.until(EC.visibility_of_element_located(selector))

      def take_screen_shot(self, prefix):
          cur_time = str(datetime.time(datetime.now()))
          current_time = cur_time.replace(":", "_").replace(".", "_")
          filename = f"{prefix}_{current_time}.png"
          if os.path.isdir(IMAGE_DIR):
              self.spdriver.save_screenshot(os.path.join(IMAGE_DIR, filename))
          else:
              os.mkdir(IMAGE_DIR)
              self.spdriver.save_screenshot(os.path.join(IMAGE_DIR, filename))

      def get_all_elements(self, selector):
          elements = self.wait.until(EC.presence_of_all_elements_located(selector))
          return elements

      def get_text_of_element(self, selector):
          element = self.wait.until(EC.presence_of_element_located(selector))
          return element.text

      def get_spdriver(self):
          if self.browser == 'chrome':
              self.spdriver = webdriver.Chrome(executable_path=chrome_driver_path)
              self.spdriver.maximize_window()
              self.spdriver.implicitly_wait(10)
          elif self.browser == 'firefox':
              self.spdriver = webdriver.Firefox(executable_path=firefox_driver_path)
              self.spdriver.maximize_window()
              self.spdriver.implicitly_wait(10)
          elif self.browser == 'edge':
              self.spdriver = webdriver.Edge(executable_path=edge_driver_path)
              self.spdriver.maximize_window()
              self.spdriver.implicitly_wait(10)




