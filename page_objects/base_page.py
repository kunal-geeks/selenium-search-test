# page_objects/base_page.py
from selenium.webdriver.common.by import By
from utilities.wait_utility import WaitUtility
from utilities.type_utility import TypeUtility

class BasePage:
    """Base Page Object Model to be inherited by other page objects."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_utility = WaitUtility(driver)
        self.type_utility = TypeUtility(driver)
    
    def get_total_entries(self, table_info_locator):
        """Fetch the total number of entries displayed."""
        total_row_text = self.driver.find_element(*table_info_locator).text
        total_entries = int(total_row_text.split()[-2])
        return total_entries
    
    def get_filtered_entries(self, table_info_locator):
        """Fetch the filtered number of entries after search."""
        total_filtered_row_text = self.driver.find_element(*table_info_locator).text
        total_filtered_row = int(total_filtered_row_text.split()[5])
        return total_filtered_row
    
    def search_for_text(self, search_box_locator, text):
        """Enter the search text into the search box."""
        self.type_utility.type_text(search_box_locator[0], search_box_locator[1], text)
    
    def get_search_results(self, row_locator):
        """Fetch the rows displayed after performing the search."""
        return self.driver.find_elements(*row_locator)
