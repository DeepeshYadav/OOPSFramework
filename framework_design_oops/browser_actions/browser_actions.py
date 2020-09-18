from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from framework_design_oops.testdata.test_data_file import *
import logging
import os

logging.basicConfig(filename=os.path.join(os.curdir, "master.log"), level=logging.DEBUG, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class BrowserAction():
      def __init__(self, browser, wait_time):
          self.browser = browser
          self.spdriver = None
          self.get_spdriver()
          self.wait = WebDriverWait(self.spdriver, wait_time)

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


      def click_element(self, selector):
          element = self.wait.until(EC.presence_of_element_located((selector[0],  selector[1] )))
          logger.debug(f"This the element on which click action would be performed : {selector}")
          element.click()

      def input_text(self, selector, value):
          logger.debug(f"This the element on which will put new data : {selector}")
          element = self.wait.until(EC.presence_of_element_located((selector[0], selector[1])))
          element.send_keys(value)




