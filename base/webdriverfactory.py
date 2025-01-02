# base/webdriverfactory.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory:
    """Factory to instantiate the appropriate WebDriver based on the browser type."""
    
    @classmethod
    def getWebDriverInstance(cls, browser="chrome"):
        if browser == "chrome":
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == "safari":
            return SafariDriver()
        else:
            raise ValueError(f"Unsupported browser specified: {browser}")
