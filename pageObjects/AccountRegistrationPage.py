from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class AccountRegistrarionPage():
    text_userID_name="username"
    text_newPassword_name="password"
    text_confirmPassword_name="repeatedPassword"
    text_firstname_name="firstName"
    text_lastname_name = "lastName"
    text_email_name = "email"
    text_phone_name = "phone"
    text_address1_xpath = "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[5]/td[2]/input[1]"
    text_address2_xpath = "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[6]/td[2]/input[1]"
    text_city_name = "city"
    text_state_name = "state"
    text_zip_name = "zip"
    text_country_name="country"
    drpdown_language_name="languagePreference"
    drpdown_category_name="favouriteCategoryId"
    chkbox_list_name="listOption"
    chkbox_banner_name="bannerOption"
    btn_saveInfo_xpath="/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/form[1]/div[1]/button[1]"
    text_msg_xpath="//div/div[1]/p"

    def __init__(self,driver):
        self.driver=driver

    def setUserID(self,UID):
        self.driver.find_element(By.NAME,self.text_userID_name).send_keys(UID)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.text_newPassword_name).send_keys(pwd)

    def setConfirmPassword(self,cpwd):
        self.driver.find_element(By.NAME,self.text_confirmPassword_name).send_keys(cpwd)

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.text_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.text_lastname_name).send_keys(lname)

    def setemail(self,email):
        self.driver.find_element(By.NAME,self.text_email_name).send_keys(email)

    def setPhone(self,phone):
        self.driver.find_element(By.NAME,self.text_phone_name).send_keys(phone)

    def setAddress1(self,address1):
        self.driver.find_element(By.XPATH,self.text_address1_xpath).send_keys(address1)

    def setAddress2(self,address2):
        self.driver.find_element(By.XPATH,self.text_address2_xpath).send_keys(address2)

    def setCity(self,city):
        self.driver.find_element(By.NAME,self.text_city_name).send_keys(city)

    def setState(self,state):
        self.driver.find_element(By.NAME,self.text_state_name).send_keys(state)

    def setZip(self,zip):
        self.driver.find_element(By.NAME,self.text_zip_name).send_keys(zip)

    def setCountry(self,country):
        self.driver.find_element(By.NAME,self.text_country_name).send_keys(country)

    def setLanguage(self,language):
        selectLang =Select(self.driver.find_element(By.NAME, self.drpdown_language_name))
        selectLang.select_by_visible_text(language)

    def setCategory(self,category):
        selectcategory= Select(self.driver.find_element(By.NAME,self.drpdown_category_name))
        selectcategory.select_by_visible_text(category)

    def setmylist(self):
        self.driver.find_element(By.NAME,self.chkbox_list_name).click()

    def setmyBanner(self):
        self.driver.find_element(By.NAME,self.chkbox_banner_name).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btn_saveInfo_xpath).click()

    def getConfirmationMessage(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_xpath).text
        except:
            None

