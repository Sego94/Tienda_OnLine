import time

class Page_Results:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.color_button = 'color_1'
        self.title_item = '//*[@id="center_column"]/ul/li/div/div[2]/h5/a'
        self.number_results = '//*[@id="center_column"]/h1/span[2]'

    def select_color_item(self):
        time.sleep(1)
        self.driver.find_element_by_id(self.color_button).click()

    def verify_text1(self):
        return self.driver.find_element_by_xpath(self.number_results).text

    def verify_text2(self):
        return self.driver.find_element_by_xpath(self.title_item).text
