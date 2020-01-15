from selenium.webdriver.common.keys import Keys

from OGtestCases.Pom.Locators.Locator import Locators


class Audio():

    def __init__(self, driver):
        self.driver = driver
        self.AudioCode_id = Locators.AudioCode_id

        self.callingParty_id = Locators.callingParty_id
        self.Search_Xpath = Locators.Search_Xpath
        self.none_Xpath = Locators.none_Xpath
        # self.search_Xpath = "//*[contains(@label,'Search')]"
        self.calling_Xpath =Locators.calling_Party_Contains_Xpath
        self.search_Xpath = Locators.Search_Xpath
        self.CalledParty = Locators.Calledparty
        self.CalledParty_2 = Locators.Called_party_idxpath
        self.StartDate = Locators.StartDate
        self.EndDate = Locators.EndDate
        self.AudioCodeRecords = Locators.Records

    def click_audioCode(self):
        self.driver.find_element_by_partial_link_text(self.AudioCode_id).click()


    def enter_CallingParty(self, callingParty_id):
        self.driver.find_element_by_id(self.callingParty_id).send_keys(callingParty_id)


    def Clear_enteredDetails(self):
        self.driver.find_element_by_id(self.callingParty_id).clear()

    def Clear_enteredDetails2(self):
        self.driver.find_element_by_id(self.CalledParty).clear()



    def enter_calledParty2(self, CallledParty_2):
        self.driver.find_element_by_xpath(self.CalledParty_2).send_keys(CallledParty_2)


    def click_Search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def click_none(self):
        self.driver.find_element_by_xpath(self.none_Xpath).click()



    def click_search(self):
       self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def click_calling_Party_Contains(self):
        self.driver.find_element_by_xpath(self.calling_Xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.Search_Xpath).click()

    def enter_CalledParty(self, CalledParty):
        self.driver.find_element_by_id(self.CalledParty).send_keys(CalledParty)
        return "Called_Party"

    def Start_Date(self):
        self.driver.find_element_by_css_selector(self.StartDate).send_keys(Keys.CONTROL, 'a', Keys.DELETE)

    def Start_Date2(self,datetime):
        self.driver.find_element_by_css_selector(self.StartDate).send_keys(datetime)
        #Start.send_keys("2019-11-22 00:00:00")

    def End_Date(self):
        self.driver.find_element_by_xpath(self.EndDate).send_keys(Keys.CONTROL, 'a', Keys.DELETE)


    def End_Date2(self, datetime2):
        self.driver.find_element_by_xpath(self.EndDate).send_keys(datetime2)
        #send_keys("2019-11-22 23:59:59")

    def Show_Records(self):
        result = self.driver.find_elements_by_xpath(self.AudioCodeRecords)
        print("Total Records",len(result))

