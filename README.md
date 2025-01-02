
# Selenium Search Functionality Testing

## Overview
This project automates the validation of search functionality on the Selenium Playground website's Table Search Demo page. The test ensures that searching for "New York" returns the expected results and validates the total number of entries on the page.

# Selenium Search Functionality Testing

## Key Highlights
- **Page Object Model (POM)**: Organized test code using POM for better maintainability and scalability.
- **Cross-browser Support**: Supports multiple browsers (Chrome, Firefox, Edge, Safari) with automated WebDriver management.
- **Search Functionality Validation**: Verifies the total number of entries and ensures correct filtering for the search term "New York."

## Features Implemented
1. **WebDriver Factory**: Manages WebDriver initialization and installation for various browsers via `webdriver-manager`.
2. **Modular Test Setup**: Utilizes pytest fixtures for reusable and scalable test setup.
3. **Reusable Utilities**: Utility classes like `WaitUtility` and `TypeUtility` enhance code readability and reusability.
4. **Test Execution with Pytest**: Provides detailed test results in the console, supporting easy debugging and tracking.

## Scope for Improvement
1. **External Test Data**: Move hardcoded test data to external files (CSV, JSON) for flexibility and scalability.
2. **Parallel Testing**: Implement parallel browser testing with tools like Selenium Grid or cloud services (e.g., LambdaTest).
3. **Enhanced Reporting**: Integrate reporting tools like **Allure** or **ExtentReports** for better test insights.
4. **Improved Error Handling**: Add checks for unexpected pop-ups and page load failures to enhance test reliability.
5. **API Test Coverage**: Extend tests to include API validations for comprehensive end-to-end testing.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kunal-geeks/selenium-search-test.git
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
pytest -s --browser=chrome
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
