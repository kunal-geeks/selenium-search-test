# page_objects/search_page.py
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class SearchPage(BasePage):
    """Page Object Model for the search functionality on the Table Search Demo page."""
    
    def __init__(self, driver):
        super().__init__(driver)  # Initialize the base page with the driver
        
        # Locators
        self.search_box_locator = (By.XPATH, "//input[@type='search']")
        self.table_info_locator = (By.ID, "example_info")
        self.row_locator = (By.XPATH, "//tr[@class='odd' or @class='even']")
    
    def get_total_entries(self):
        """Fetch the total number of entries displayed."""
        return super().get_total_entries(self.table_info_locator)
    
    def get_filtered_entries(self):
        """Fetch the filtered number of entries after search."""
        return super().get_filtered_entries(self.table_info_locator)
    
    def search_for_text(self, text):
        """Enter the search text into the search box."""
        super().search_for_text(self.search_box_locator, text)
    
    def get_search_results(self):
        """Fetch the rows displayed after performing the search."""
        return super().get_search_results(self.row_locator)
