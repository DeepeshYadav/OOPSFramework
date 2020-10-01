import os
browser = 'chrome'
#url = "https://www.google.co.in"
url = "https://www.goibibo.com/"
search_value = "Selenium"
wait_time = 20


chrome_driver_path = "E:\\driver\\chromedriver.exe"
firefox_driver_path = "E:\\driver\\geckodriver.exe"
edge_driver_path = "E:\\driver\\msedgedriver.exe"


CUR_DIR = os.getcwd()
LOG_DIR = os.path.join(CUR_DIR, 'log')
IMAGE_DIR = os.path.join(CUR_DIR, 'image')
test_data_path = os.path.join(CUR_DIR, 'testdata')
excel_file_path = os.path.join(test_data_path, 'test_data_excel.xlsx')

HOTEL_LOCATION = 'Navi Mumbai'
check_in_date  = 27
check_out_date = 30
rooms = 5
adults = 10
childs = 5