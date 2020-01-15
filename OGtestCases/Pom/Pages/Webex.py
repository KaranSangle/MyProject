from OGtestCases.Pom.Locators.Locator import Locators
class Webex_test():


    def __init__(self, driver):
        self.driver = driver

        self.Webex_by_partial_link_text = Locators.Webex_by_partial_link_text
        self.CallingParty_id = Locators.CallingParty_id
        self.Search_Xpath = Locators.Search_Xpath
        self.none_Xpath = Locators.none_Xpath
        # self.search_Xpath = "//*[contains(@label,'Search')]"
        self.calling_Xpath = Locators.calling_Xpath
        self.search_Xpath = "//*[contains(@label,'Search')]"
       # self.meeting_Xpath = "//*[contains(@inputid,'meetingKey')]"

        #self.CalledParty = "calledParty-id"



    def Select_Webex(self):
        self.driver.find_element_by_partial_link_text(self.Webex_by_partial_link_text).click()


    def enter_CallingParty(self, callingParty_id):
        self.driver.find_element_by_id(self.CallingParty_id).send_keys(callingParty_id)

    def click_Search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def click_none(self):
        self.driver.find_element_by_xpath(self.none_Xpath).click()

    #
    # def click_search(self):
    #     self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def click_calling(self):
        self.driver.find_element_by_xpath(self.calling_Xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def enter_CalledParty(self, CalledParty):
        self.driver.find_element_by_id(self.CalledParty).send_keys(CalledParty)








