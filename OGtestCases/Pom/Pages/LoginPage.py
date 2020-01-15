from selenium import webdriver


class LoginPage():

    def __init__(self, driver):#constructor
        self.driver = driver
        self.username_id = "username"
        self.password_id = "password"
        self.login_button_id = "kc-login"
        self.logout_button_id= "logout-id"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def click_logout_button(self):
        self.driver.find_element_by_id(self.logout_button_id).click()

