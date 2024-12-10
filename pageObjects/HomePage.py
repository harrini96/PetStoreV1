from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage():

    link_cart_name="img_cart"
    link_login_linktext = "Sign In"
    link_register_linktext="Sign Up"
    link_help_linktext="?"
    txtbox_search_xpath="//input[@placeholder='Product Search']"
    btn_search_xpath="//button[normalize-space()='Search']"


    def __init__(self,driver):
        self.driver=driver

    def clickCart(self):
        self.driver.find_element(By.XPATH,self.link_cart_name).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.link_login_linktext).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.link_register_linktext).click()

    def clickHelp(self):
        self.driver.find_element(By.LINK_TEXT,self.link_help_linktext).click()

    def typeSearch(self,searchtxt):
        self.driver.find_element(By.LINK_TEXT,self.txtbox_search_xpath).send_keys(searchtxt)

    def clickSearch(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_search_xpath).click()



