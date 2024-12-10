from time import sleep

import pytest

from pageObjects.HomePage import *
from pageObjects.AccountRegistrationPage import *
from utilities import randomString
from utilities import readProperties
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen




class Test_001_accountRegistration:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    print(baseURL)

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()
        # sleep(10)

        self.hp=Homepage(self.driver)
        self.hp.clickRegister()
        self.logger.info("Clicking on Register")
        # sleep(5)

        self.regpage=AccountRegistrarionPage(self.driver)
        self.logger.info("Registering by giving user details")
        self.userid=randomString.random_string_generator()
        self.regpage.setUserID(self.userid)
        # self.regpage.setUserID("user111")
        self.regpage.setPassword("user111")
        self.regpage.setConfirmPassword("user111")
        self.regpage.setFirstName("rick")
        self.regpage.setLastName("john")
        self.regpage.setemail("rickjohn@gmail.com")
        # self.regpage.setemail("rickjohn")
        # self.email=randomString.random_string_generator()+"@gmail.com"
        # self.regpage.setemail(self.email)
        self.regpage.setPhone("99999991111")
        self.regpage.setAddress1("Address line 1")
        self.regpage.setAddress2("Address line 2")
        self.regpage.setCity("city1")
        self.regpage.setState("state1")
        self.regpage.setZip("123456")
        self.regpage.setCountry("country1")
        self.regpage.setLanguage("German")
        self.regpage.setCategory("Birds")
        self.regpage.setmylist()
        self.regpage.setmyBanner()
        self.regpage.clickSave()
        self.confirmMsg=self.regpage.getConfirmationMessage()
        print(self.confirmMsg)
        sleep(10)

        if self.confirmMsg=="Your account has been created. Please try login.":
            self.logger.info("Registration successful")
            assert True
            self.driver.close()
        else:
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"\\test_account_reg.png")
            self.logger.error("Registration failed")
            self.driver.close()
            assert False
