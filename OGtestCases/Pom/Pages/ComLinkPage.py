from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from OGtestCases.Pom.Locators.Locator import Locators


class ComLPage():

    def __init__(self, driver):

        self.driver = driver

        self.Comlink_id = Locators.Comlink_id
        self.callingParty_id = Locators.ComcallingParty_id
        self.Search_Xpath = Locators.Search_Xpath
        self.none_Xpath = Locators.Comnone_Xpath
        # self.search_Xpath = "//*[contains(@label,'Search')]"
        self.calling_Xpath = Locators.Comcalling_Party_Contains_Xpath
        self.search_Xpath = Locators.search_Xpath
        self.CalledParty = Locators.ComCalledparty
        self.CalledParty_2 = Locators.ComCalled_party_idxpath
        self.StartDatexpath = Locators.ComStartDate
        self.EndDatexpath = Locators.ComEndDate1
        self.comlinkCodeRecords = Locators.Records


    def Select_ComLink(self):
        self.driver.find_element_by_xpath(self.Comlink_id).click()

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

    def ComLink_click_search(self):
        self.driver.find_element_by_xpath(self.search_Xpath).click()

    def enter_CalledParty(self, CalledParty):
        self.driver.find_element_by_id(self.CalledParty).send_keys(CalledParty)

    def ComLink_Start_Date(self):
        #self.driver.find_element_by_xpath(self.StartDatexpath).click()
        self.driver.find_element_by_xpath(self.StartDatexpath).send_keys(Keys.CONTROL, 'a', Keys.DELETE)

    def ComLink_Start_Date2(self, datetime):
        self.driver.find_element_by_xpath(self.StartDatexpath).send_keys(datetime)
        # Start.send_keys("2019-11-22 00:00:00")

    def ComLink_End_Date(self):
        #self.driver.find_element_by_xpath(self.EndDatexpath).click()
        self.driver.find_element_by_xpath(self.EndDatexpath).send_keys(Keys.CONTROL, 'a', Keys.DELETE)

    def ComLink_End_Date2(self, datetime2):
        self.driver.find_element_by_xpath(self.EndDatexpath).send_keys(datetime2)
        # send_keys("2019-11-22 23:59:59")

    def Show_Records(self):
        result = self.driver.find_elements_by_xpath(self.comlinkCodeRecords)
        print("Total Records", len(result))

