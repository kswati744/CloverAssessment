import pytest
from selenium import webdriver
from pageObjects.searchEngine import Search_engines
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

@pytest.mark.usefixtures("setup")

class TestSearchEngine:
    GoogleUrl = ReadConfig.getGoogleURL()
    BingUrl = ReadConfig.getBingURL()
    logger=LogGen.loggen()
    default_search_text = ReadConfig.getDefaultSearchText()
    GoogleEngineName = ReadConfig.getGoogleEngineName()
    BingEngineName = ReadConfig.getBingEngineName()

    @pytest.mark.sanity
    def test_google_search(self,setup):

        self.logger.info("*******************TestSearchEngine*********************")
        self.logger.info("Validating first returned item from Google Search Engine: " )
        self.driver=setup
        self.driver.get(self.GoogleUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("reached")
        search_engine = Search_engines(self.driver, self.logger)
        search_button_element_id = search_engine.input_text_search_box(self.default_search_text,self.GoogleEngineName)

        if search_button_element_id:
            search_engine.press_enter_key(search_button_element_id)
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"SearchEngineResultGoogle.png")
            self.logger.error("Not able to enter text")
        self.logger.info("Trying to get first result")
        first_result = search_engine.get_first_search_result(self.GoogleEngineName)
        if first_result:
            self.logger.info(first_result)
            assert self.default_search_text in first_result["Title"],"Google search result validation failed"

    @pytest.mark.sanity
    def test_Bing_search(self,setup):

        self.logger.info("*******************TestSearchEngine*********************")
        self.logger.info("Validating first returned item from Bing Search Engine: " )
        self.driver=setup
        self.driver.get(self.BingUrl)
        self.driver.maximize_window()
        time.sleep(5)
        self.logger.info("reached")
        search_engine = Search_engines(self.driver, self.logger)
        search_button_element_id = search_engine.input_text_search_box(self.default_search_text,self.BingEngineName)

        if search_button_element_id:
            search_engine.press_enter_key(search_button_element_id)
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"SearchEngineResultBing.png")
            self.logger.error("Not able to enter text")
        self.logger.info("Trying to get first result")
        first_result = search_engine.get_first_search_result(self.BingEngineName)
        if first_result:
            self.logger.info(first_result)
            assert self.default_search_text in first_result["Title"],"Bing search result validation failed"


