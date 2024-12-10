import pytest
from pageObjects.HomePage import *
from pageObjects.LoginPage import *
from utilities.customLogger import LogGen
import os
from utilities.readProperties import ReadConfig

class Test_002LoginPage():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    userId=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*** test_002_LoginPage started ***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=Homepage(self.driver)
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setUserId(self.userId)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isPetFavouritePageExist()
        if self.targetpage==True:
            self.logger.info("Login Success")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            self.logger.error("Login failed")
            assert False

        self.driver.close()

