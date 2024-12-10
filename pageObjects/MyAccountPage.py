from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountPage():
    link_logout_linktext="Sign Out"

    def __init__(self,driver):
        self.driver=driver

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
