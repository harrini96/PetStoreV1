from time import sleep
import pytest

from pageObjects.HomePage import *
from pageObjects.LoginPage import *
from pageObjects.MyAccountPage import *
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import os

class Test_LoginFromExcel():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path=os.path.abspath(os.curdir)+"\\testData\\LoginPetStore.xlsx"

    def test_loginfromexcel(self,setup):
        self.logger.info("*** test_003_LoginFromExcel started ***")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]                                                 #empty list to get the status of the test results(comparing the login with excel sheet)

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=Homepage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ma=MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.hp.clickLogin()

            self.userid=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setUserId(self.userid)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            sleep(5)
            self.targetpage=self.lp.isPetFavouritePageExist()

            if self.exp=='valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='invalid':
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')

        print(lst_status)
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("***end of test_003_loginFromExcel")