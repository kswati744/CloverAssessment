CLOVER

My requirement: Create a test framework using any language and tool(s) that does the following:
1. Visit one or more search engine(s); i.e google, bing, yahoo, etc...
2. Submit a search term
3. On the results page, take the first returned item and assert it as the expected result.

Framework Overview:

This is Selenium-based testing framework which incorporates the Page Object Model (POM) design pattern, offering robust and maintainable UI automation testing. The framework is structured to enhance code readability, reusability, and maintainability, making it suitable for large-scale and complex web applications.

Key Components:

Page Object Model (POM): Implements a layered architecture for web pages, promoting separation of concerns and reducing code duplication.
Test Cases: Well-defined test scripts focusing on specific functionalities and scenarios, ensuring comprehensive coverage.
Pytest Configuration (pytest.ini)
pytest.ini is used to define custom markers and general test behavior settings. 
conftest.py contains setup configurations for your tests, including browser setup. It defines fixtures for initializing and tearing down browser instances.And allows you to pass the browser type as a command-line argument when running tests.

Utilities:

Custom Logger:('customLogger.py') Facilitates tracking of test execution and aids in debugging with detailed logs.
ReadProperties: ('readProperties.py') Manages external configuration, allowing easy modification of test parameters.
Pytest-HTML Reports: Generates visually appealing and informative test execution reports.
Logs: Provides a persistent and detailed record of test runs for troubleshooting and historical analysis.
Configuration Management (Config.ini): Centralizes test environment and setup configurations, enhancing flexibility and scalability.

Command to execute the Testcase -  pytest -v -m "sanity" --html=./Reports/report.html testCases/testSearchResults.py --browser chrome
