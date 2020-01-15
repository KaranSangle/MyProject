from OGtestCases.Pom.Locators.Locator import Locators


class Sns_test:

    def __init__(self, driver):
        self.driver = driver

        self.Sns_by_partial_link_text = Locators.Sns_by_partial_link_text
        self.CallingParty_id = Locators.callingParty_id
        self.Search_Xpath = Locators.Search_Xpath
        self.none_Xpath = Locators.none_Xpath
        self.calling_Party_Xpath = Locators.calling_Party_Contains_Xpath
        self.search_Xpath = Locators.search_Xpath
        self.CalledParty = Locators.Calledparty
        self.click_telechemy = Locators.Click_telechemy
        self.Telechemy_id = Locators.telechemy123

    def Select_Sns(self):
        self.driver.find_element_by_partial_link_text(self.Sns_by_partial_link_text).click()

    def enter_CallingParty(self, CallingParty_id):
        self.driver.find_element_by_id(self.CallingParty_id).send_keys(CallingParty_id)

    def click_Search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def click_none(self):
        self.driver.find_element_by_xpath(self.none_Xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def Clear_enteredDetails(self):
        self.driver.find_element_by_id(self.CallingParty_id).clear()

    def click_calling_Party_Contains(self):
        self.driver.find_element_by_xpath(self.calling_Party_Xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def enter_CalledParty(self, CalledParty):
        self.driver.find_element_by_id(self.CalledParty).send_keys(CalledParty)

    def click_telechemyxpath(self):
        self.driver.find_element_by_xpath(self.click_telechemy).click()

    def Telechemy(self, telechemy):
        self.driver.find_element_by_id(self.Telechemy_id).send_keys(telechemy)
