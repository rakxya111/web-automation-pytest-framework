from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.product_page import ProductPage


class ProductMenuPage:

    inventory = (By.XPATH, "//a[.//span[text()='Inventory']]")
    product = (By.XPATH, "//a[normalize-space()='Products']")
    product_list = (By.XPATH, "//a[normalize-space()='Product List']")

    def __init__(self, driver , wait):
        self.driver = driver
        self.wait = wait

    def go_to_productpage(self):
        inventory_field = self.wait.until(
            EC.element_to_be_clickable(
                (self.inventory)
            )
        )
        inventory_field.click()

        product_page = self.wait.until(
            EC.element_to_be_clickable(
                (self.product)
            )
        )
        product_page.click()

        product_list_page = self.wait.until(
            EC.element_to_be_clickable(
                (self.product_list)
            )
        )
        product_list_page.click()

        return ProductPage(self.driver, self.wait)
