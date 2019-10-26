from selenium import webdriver

class BrowserFactory():

    def __init__(self):
        """"""
        
    def getDriver(self, browser):
        """"""
        if browser.lower()=="chrome":
            self.driver=webdriver.Chrome()
            return self.driver
        elif browser.lower()=="explorer":
            self.driver=webdriver.Ie()
            return self.driver
        elif browser.lower()=="firefox":
            self.driver=webdriver.Firefox()
            return self.driver