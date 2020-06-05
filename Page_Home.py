import time

class Page_Home:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_box = 'search_query_top'
        self.search_button = 'submit_search'
        self.text_call_us = '//*[@id="cmsinfo_block"]/div[1]/ul/li[2]/div/h3'

    def search_a_item(self, text):
        self.driver.find_element_by_id(self.search_box).send_keys(text)
        time.sleep(1)
        self.driver.find_element_by_name(self.search_button).click()

    def verify_text(self):
        return self.driver.find_element_by_xpath(self.text_call_us).text




