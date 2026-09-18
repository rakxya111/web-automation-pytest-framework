from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CatgoryPage:

    add_catgory_button = (By.XPATH, "//button[normalize-space()='Add']")
    category_name = (By.ID, "name")
    cost_center_dropdown =  (By.CSS_SELECTOR, "div[id='costCenterId'] div[class='css-1xc3v61-indicatorContainer']")
    cost_center_firstOption = (By.XPATH, "//div[contains(@id,'react-select-') and contains(@id,'-option-0')]")
    save_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self , driver , wait):
        self.driver = driver
        self.wait = wait

    def click_add_category(self):
        add_category = self.wait.until(
            EC.element_to_be_clickable(
                (self.add_catgory_button)
            )
        )
        add_category.click()

    def enter_category_name(self, name):
        category = self.wait.until(
            EC.visibility_of_element_located(
                (self.category_name)
            )
        )
        category.send_keys(name)

    def select_first_cost_center(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (self.cost_center_dropdown)
            )
        )
        dropdown.click()

        firstOption = self.wait.until(
            EC.element_to_be_clickable(
                (self.cost_center_firstOption)
            )
        )
        firstOption.click()

    def click_save(self):
        save = self.wait.until(
            EC.element_to_be_clickable(
                (self.save_button)
            )
        )
        save.click()

    def add_category(self, category_name):
        self.click_add_category()
        self.enter_category_name(category_name)
        self.select_first_cost_center()
        self.click_save()
    


