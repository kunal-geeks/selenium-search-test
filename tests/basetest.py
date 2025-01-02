# tests/basetest.py
import pytest
from base.webdriverfactory import WebDriverFactory
from utilities.logger import get_logger

class BaseTest:
    @pytest.fixture(scope="class")
    def oneTimeSetUp(self, request):
        """This will run once per test class."""
        print("Running class setUp")

        # Get the browser value from pytest or default to "chrome"
        browser = request.config.getoption("--browser", default="chrome").lower()

        # Create an instance of WebDriverFactory and get the appropriate driver
        driver = WebDriverFactory.getWebDriverInstance(browser)

        # Attach the driver to the class so tests can access it
        if request.cls is not None:
            request.cls.driver = driver

        yield driver  # This allows the tests to run

        driver.quit()  # Clean up and quit the driver after all tests are finished
        print("\n Running class tearDown")

    @pytest.fixture(autouse=True)
    def setup_method(self, oneTimeSetUp):
        """Setup method for each test."""
        self.driver = oneTimeSetUp  # Make sure the driver is available for the test
        self.logger = get_logger()  # Initialize the logger
        self.logger.info("Test setup completed.")
