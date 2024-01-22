import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class Search_engines:
    search_input_locators = {
        "Google": (By.NAME, "q"),
        "Bing": (By.ID, "sb_form_q")
    }
    search_results_locators = {
        "Google": (By.CSS_SELECTOR, "div#search div.g"),
        "Bing": (By.XPATH, "//*[@id='b_results']/li")
    }
    title_tag = {
        "Google": "h3",
        "Bing": "h2"
    }
    link_locator = (By.TAG_NAME, "a")


    def __init__(self,driver,logger):
        self.logger = logger
        self.driver = driver

    def input_text_search_box(self,text,engine_name):
        self.logger.info("reached inside")
        try:
            locator_type, locator_value = self.search_input_locators[engine_name]
            self.logger.info("reached inside try")
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((locator_type, locator_value)))
            search_input.clear()
            search_input.send_keys(text)
            self.logger.info(f"Text '{text}' entered in search box on {engine_name}")
            return search_input
        except Exception as e:
            self.logger.info(f"Error finding search box on {engine_name}: {e}")
            return None

    def press_enter_key(self,search_input):

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(search_input).send_keys(Keys.ENTER).perform()
            time.sleep(5)
            self.logger.info("Enter key pressed")
        except Exception as e:
            self.logger.error(f"Error pressing enter key: {e}")

    def get_first_search_result(self,engine_name):
        try:
            if engine_name == "Google":
                locator = (By.CSS_SELECTOR, "div#search div.g")
            elif engine_name == "Bing":
                locator = (By.XPATH, "//*[@id='b_results']/li")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
            self.logger.info("Trying to find search results")
            search_results = self.driver.find_elements(*locator)
            self.logger.info(f"Got results")
            if not search_results:
                self.logger.info(f"No search results found on {engine_name}.")
                return "-----------FAILED----------"

            first_result = search_results[0]
            self.logger.info("Got first search result")
            title_tag = self.title_tag[engine_name]
            title = first_result.find_element(By.TAG_NAME, title_tag).text
            link = first_result.find_element(*self.link_locator).get_attribute('href')

            return {"Title": title, "Link": link}

        except Exception as e:
            self.logger.error(f"Error retrieving search results from {engine_name}: {e}")
        return None







