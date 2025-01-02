import logging
from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility
from utilities.logger import get_logger

logger = get_logger()

class TypeUtility:
    """
    Utility class to handle typing actions in Selenium.
    """

    def __init__(self, driver):
        """
        Initialize the TypeUtility with a WebDriver instance.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait_utility = WaitUtility(driver)

    def type_text(self, locator_type, locator, text):
        """
        Wait for an element to be visible and type text into it.

        :param locator_type: Type of locator (e.g., By.ID, By.XPATH)
        :param locator: Locator value
        :param text: Text to be typed into the element
        """
        try:
            logger.info(f"Waiting for element with locator: {locator} to be visible.")
            element = self.wait_utility.wait_for_element_visible(locator_type, locator)
            logger.info(f"Element found: {locator}. Clearing existing text and typing new text.")
            element.clear()  # Clear existing text if any
            element.send_keys(text)
            logger.info(f"Text '{text}' typed into element: {locator}")
        except Exception as e:
            logger.error(f"An error occurred while typing text into element {locator}: {str(e)}")
            raise

    def append_text(self, locator_type, locator, text):
        """
        Wait for an element to be visible and append text into it.

        :param locator_type: Type of locator (e.g., By.ID, By.XPATH)
        :param locator: Locator value
        :param text: Text to append to the existing value in the element
        """
        try:
            logger.info(f"Waiting for element with locator: {locator} to be visible.")
            element = self.wait_utility.wait_for_element_visible(locator_type, locator)
            logger.info(f"Element found: {locator}. Appending text.")
            element.send_keys(text)
            logger.info(f"Text '{text}' appended to element: {locator}")
        except Exception as e:
            logger.error(f"An error occurred while appending text to element {locator}: {str(e)}")
            raise
