from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.category_page import CatgoryPage

class DashboardPage:

    inventory = (By.XPATH, "//a[.//span[normalize-space()='Inventory']]")
    category = (By.CSS_SELECTOR, ".nav-link[href='/category-list']")

    def __init__(self , driver , wait):
        self.driver = driver
        self.wait = wait

    def go_to_inventory(self):
        inventory_field = self.wait.until(
            EC.element_to_be_clickable(
                (self.inventory)
            )
        )
        inventory_field.click()

    def go_to_category(self):
        self.go_to_inventory()
        category_field = self.wait.until(
            EC.element_to_be_clickable(
                (self.category)
            )
        )
        category_field.click()

        category_page = CatgoryPage(self.driver, self.wait)
        return category_page
    
    
        