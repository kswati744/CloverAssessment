import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.data_fetcher import load_test_data
from utils.driver_setup import get_driver


def test_search_functionality(excel_file):
    test_data = load_test_data(excel_file)
    for index, row in test_data.iterrows():
        driver = get_driver()
        driver.get(row['SearchSite'])

        if "google" in row['SearchSite'] or "bing" in row['SearchSite']:
            search_box = driver.find_element(By.NAME, "q")
        elif "yahoo" in row['SearchSite']:
            search_box = driver.find_element(By.NAME, "p")
        else:
            raise ValueError("Unsupported search engine")

        search_box.send_keys(row['SearchQuery'])
        search_box.send_keys(Keys.RETURN)

        assert row['ExpectedResult'] in driver.page_source

        driver.quit()


@pytest.fixture
def excel_file(request):
    return request.config.getoption("--excel")
