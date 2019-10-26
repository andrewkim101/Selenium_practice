from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_verify_title(self):
        self.driver.get(("https://google.com"))
        time.sleep(4)
        print(self.driver.current_url)
        print(self.driver.title)
        google_title=self.driver.title
        assert(google_title=="Google")
        # if self.driver.title=="Google":
        #     print(True)
        # else:
        #     print(False)
        

    def temp_test_search_box(self):
        self.driver.set_page_load_timeout("10")
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step with Python")
        time.sleep(5)
        self.driver.find_element_by_name('btnK').submit()
        time.sleep(4)
    
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    #     print("Test complited")

if __name__ == "__main__":
    unittest.main(verbosity=2)