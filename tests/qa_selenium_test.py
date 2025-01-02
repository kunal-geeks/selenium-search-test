# tests/test_search.py
import pytest
from page_objects.search_page import SearchPage
from tests.basetest import BaseTest

class TestSearchFunctionality(BaseTest):

    def test_search_functionality(self):
        """Test the search functionality on the Selenium Playground Table Search Demo."""
        search_page = SearchPage(self.driver)  # Use the driver from the BaseTest

        self.logger.info("Navigating to the Selenium Playground Table Search Demo page.")
        self.driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

        # Validate the total number of entries
        self.validate_total_entries(search_page)

        # Perform search for "New York" and validate results
        self.perform_and_validate_search(search_page, "New York", expected_filtered_entries=5)

    def validate_total_entries(self, search_page):
        """Validate the total number of entries on the page."""
        self.logger.info("Validating total entries.")
        total_entries = search_page.get_total_entries()
        self.logger.info(f"Total entries found: {total_entries}")
        assert total_entries == 24, f"Expected total entries to be 24, but found {total_entries}"

    def perform_and_validate_search(self, search_page, search_text, expected_filtered_entries):
        """Perform the search and validate the results."""
        # Perform search
        self.logger.info(f"Performing search for '{search_text}'.")
        search_page.search_for_text(search_text)

        # Get filtered results
        self.logger.info(f"Validating search results for '{search_text}'.")
        filtered_rows = search_page.get_search_results()
        total_filtered_entries = search_page.get_filtered_entries()
        self.logger.info(f"Filtered entries found: {total_filtered_entries}")

        # Assert filtered entries match the expected count
        assert total_filtered_entries == expected_filtered_entries, \
            f"Expected {expected_filtered_entries} entries, but found {total_filtered_entries}"
        assert len(filtered_rows) == total_filtered_entries, \
            f"Expected {total_filtered_entries} entries, but found {len(filtered_rows)}"
