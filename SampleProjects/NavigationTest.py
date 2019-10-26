from selenium import webdriver
from BrowserFactory import BrowserFactory
from StringUtility import StringUtility

class NavigationTest():
    """"""
    def __init__(self, browser):
        """"""
        self.browser=browser
        
    def test(self):
        self.driver=BrowserFactory.getDriver(self.browser)
        self.driver.get("https://google.com")
        title=self.driver.title()
        self.driver.navigate().to("https://etsy.com")
        title2=self.driver.title()
        self.driver.navigate().back()
        StringUtility.verigyEquals(title,self.driver.title())
        self.driver.navigate().forward()
        StringUtility.verigyEquals(title2,self.driver.title())

    


chrome=NavigationTest("chrome")
chrome.test()
firefox=NavigationTest("firefox")
chrome.test()
explorer=NavigationTest("explorer")
chrome.test()



