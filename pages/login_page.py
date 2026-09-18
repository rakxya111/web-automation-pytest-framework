from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from pages.dashboard_page import DashboardPage

class LoginPage:

    username = (By.CSS_SELECTOR, "div[class='p-2 py-4'] input[placeholder='Enter email']")
    password = (By.CSS_SELECTOR, "div[class='p-2 py-4'] input[placeholder='Enter Password']")
    button_login = (By.CSS_SELECTOR, "div[class='p-2 py-4'] button[type='submit']")
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.password)
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.button_login)
        )
        login_button.click()

    def login(self, username , password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
