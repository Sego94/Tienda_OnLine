#TRABAJO DE CLASE 5: Meter ropa en el carrito
#1-Buscar por T-shirts
#2-Al elemento que aparece, le clickean el color naranja
#3-Poner 25 en cantidad
#4-Clickear 3 veces el boton +
#5-Verificar que el numero que aparece es 28

import unittest
import time
from selenium import webdriver
from Page_Home import Page_Home
from Page_Search_Results import Page_Results
from Page_Item import Page_Item


class Add_cart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.page_home = Page_Home(self.driver)
        self.assertEqual(self.page_home.verify_text(), 'Call Us')
        self.page_resulst = Page_Results(self.driver)
        self.page_item = Page_Item(self.driver)

    def test01_Add_cart(self):
        self.page_home.search_a_item('t-shirt')
        self.assertTrue('result has been found' in self.page_resulst.verify_text1())
        self.assertEqual(self.page_resulst.verify_text2(), 'Faded Short Sleeve T-shirts')
        self.page_resulst.select_color_item()
        self.assertEqual(self.page_item.verify_name_item(), 'Faded Short Sleeve T-shirts')
        self.assertEqual(self.page_item.verify_quantity_text(), 'Quantity')
        self.page_item.quantity_item('25')
        self.assertEqual(self.page_item.verify_num_box_quantity(), '28')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
