import time


class Page_Item:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.name_item = '//*[@id="center_column"]/div/div/div[3]/h1'
        self.quantity_text = '//*[@id="quantity_wanted_p"]/label'
        self.quantity_box = 'quantity_wanted'
        self.add_button = '//*[@id="quantity_wanted_p"]/a[2]/span'
        self.add_cart_button = '//*[@id="add_to_cart"]/button/span'
        self.cross_button = '//span[contains(@class,"cross")]'
        self.num_item = '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]'

    def quantity_item(self, num):
        time.sleep(1)
        self.driver.find_element_by_id(self.quantity_box).clear()
        self.driver.find_element_by_id(self.quantity_box).send_keys(num)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.add_button).click()
        self.driver.find_element_by_xpath(self.add_button).click()
        self.driver.find_element_by_xpath(self.add_button).click()
        self.driver.find_element_by_xpath(self.add_cart_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.cross_button).click()

    def verify_name_item(self):
        return self.driver.find_element_by_xpath(self.name_item).text

    def verify_quantity_text(self):
        return self.driver.find_element_by_xpath(self.quantity_text).text

    def verify_num_box_quantity(self):
        return self.driver.find_element_by_xpath(self.num_item).text







