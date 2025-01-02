from utilities.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = get_logger()

class WaitUtility:
    """
    Utility class to handle various wait operations in Selenium.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize the WaitUtility with a WebDriver instance.

        :param driver: Selenium WebDriver instance
        :param timeout: Timeout duration for waiting operations (default 10 seconds)
        """
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator_type, locator):
        """
        Wait for an element to be visible on the page.
        """
        try:
            logger.info(f"Waiting for visibility of element with locator: {locator}")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((locator_type, locator))
            )
            logger.info(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for visibility of element with locator: {locator}")
            raise TimeoutException

    def wait_for_element_clickable(self, locator_type, locator):
        """
        Wait for an element to be clickable on the page.
        """
        try:
            logger.info(f"Waiting for element to be clickable with locator: {locator}")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((locator_type, locator))
            )
            logger.info(f"Element is clickable: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for element to be clickable with locator: {locator}")
            raise TimeoutException

    def wait_for_element_present(self, locator_type, locator):
        """
        Wait for an element to be present in the DOM.
        """
        try:
            logger.info(f"Waiting for presence of element with locator: {locator}")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((locator_type, locator))
            )
            logger.info(f"Element present: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for presence of element with locator: {locator}")
            raise TimeoutException

    def wait_for_elements_present(self, locator_type, locator):
        """
        Wait for multiple elements to be present in the DOM.
        """
        try:
            logger.info(f"Waiting for presence of multiple elements with locator: {locator}")
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((locator_type, locator))
            )
            logger.info(f"Found {len(elements)} elements with locator: {locator}")
            return elements
        except TimeoutException:
            logger.error(f"Timed out waiting for presence of elements with locator: {locator}")
            raise TimeoutException
