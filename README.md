
# Selenium Search Functionality Testing

## Overview
This project automates the validation of search functionality on the Selenium Playground website's Table Search Demo page. The test ensures that searching for "New York" returns the expected results and validates the total number of entries on the page.

## Key Highlights
- **Page Object Model (POM)**: The project follows the Page Object Model design pattern, creating distinct classes for different pages (e.g., SearchPage) that encapsulate page-specific actions and locators. This improves maintainability and scalability.
- **Modular Test Setup**: WebDriver management and browser configuration are abstracted through a `WebDriverFactory` class and pytest fixtures. The setup supports multiple browsers (Chrome, Firefox, Edge, Safari).
- **Search Functionality Test**: The test case checks the following:
  1. Verifies the total number of entries on the page.
  2. Validates that performing a search for "New York" returns the correct number of filtered results.

## Features Implemented
1. **WebDriver Factory**: Automatically manages the installation and initialization of WebDriver for multiple browsers using `webdriver-manager`.
2. **Test Reporting with Pytest**: Uses `pytest` for test execution, providing detailed output in the console. This makes it easy to track test results and failures.
3. **Reusable Utilities**: The project contains reusable utility classes like `WaitUtility` and `TypeUtility` for waiting and typing actions, which improves code readability and reduces redundancy.
4. **Modular Page Object Model (POM)**: The `SearchPage` class defines locators and actions related to the search functionality, making the tests easier to maintain and extend.

## Scope for Improvement
1. **Test Data Management**: Currently, test data is hardcoded. It would be beneficial to externalize the test data (e.g., via CSV, JSON, or a database) to make the tests more flexible and easier to scale.
2. **Cross-browser Testing**: While the project supports different browsers, it can be improved by running parallel tests across browsers using tools like Selenium Grid or a cloud service like Sauce Labs or LambdaTest.
3. **Enhanced Reporting**: Currently, the project uses console logs for reporting. Incorporating a full-fledged reporting tool like **Allure** or **ExtentReports** would provide better visualization and insights for test results.
4. **Error Handling**: Additional checks and better error handling in case of unexpected pop-ups, alerts, or page load failures could improve the reliability of tests.
5. **API Tests**: Extending the testing scope to include API tests using `requests` or other tools would ensure complete end-to-end validation.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd selenium-search-test
```

### 2. Set Up a Virtual Environment (Optional)
Create and activate a virtual environment to manage dependencies:
#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scriptsctivate
```

### 3. Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Test
To run the search functionality test:
```bash
pytest tests/test_search_functionality.py -v
```

### Expected Output
- **Search Validation**: The test will validate that searching for "New York" returns exactly 5 visible entries and that the table has a total of 24 entries.

## Dependencies
The following Python libraries are used in this project:
- **selenium**: For browser automation.
- **webdriver-manager**: To automatically manage the WebDriver for browsers.
- **pytest**: For test execution and reporting.

You can install all dependencies with:
```bash
pip install -r requirements.txt
```

## Notes
- **WebDriver**: The project uses `webdriver-manager` to automatically download the necessary WebDriver for Chrome, Firefox, or Edge. Ensure your browser is up-to-date.
- **Browser Compatibility**: The tests are set up for Chrome by default, but you can specify another browser via the `--browser` argument when running the test.

## Troubleshooting

1. **Dependency Issues**:
   - Ensure all dependencies are installed correctly by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Browser Issues**:
   - Ensure the selected browser is installed and up-to-date.
   - If using a different browser, update the WebDriver setup in `qa_selenium_test.py`.

3. **Locator Issues**:
   - If the page structure changes, update the locators in `test_search_functionality.py`.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

### Need Help?
If you encounter any issues or have questions, please open an issue on the repository's issue tracker.
