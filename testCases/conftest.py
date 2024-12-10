import os
from datetime import datetime

import pytest
from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser=="edge":
        from selenium.webdriver.edge.service import Service
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Edge..")
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Firefox..")
    else:
        from selenium.webdriver.chrome.service import Service
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Chrome..")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############ pytest HTML reports ###########

# #hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['project Name']='PetStore'
#     config._metadata['Module Name']='Registration'

#Hook for deleting/modifying environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

#specify report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+'\\reports\\'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+'.html'
    # config.option.htmlpath = "C:\\Users\\arunp\\PetStoreV1\\reports" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"