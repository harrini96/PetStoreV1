from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    txt_email_name="username"
    txt_password_name="password"
    btn_login_xpath="//button[normalize-space()='Login']"
    msg_petfavourite_linktext="My Account"

    def __init__(self,driver):
        self.driver=driver

    def setUserId(self,userId):
        self.Id=self.driver.find_element(By.NAME,self.txt_email_name)
        self.Id.clear()
        self.Id.send_keys(userId)

    def setPassword(self,password):
        self.password=self.driver.find_element(By.NAME,self.txt_password_name)
        self.password.clear()
        self.password.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isPetFavouritePageExist(self):
        try:
           return self.driver.find_element(By.LINK_TEXT,self.msg_petfavourite_linktext).is_displayed()
        except:
            return False
