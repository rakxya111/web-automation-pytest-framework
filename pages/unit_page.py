from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UnitPage:
    add_unit_link = (By.XPATH, "//button[normalize-space()='Add']")
    unit_name =  (By.ID, "name")
    unit_code = (By.ID, "code")
    unit_ratio = (By.ID, "ratio")
    unit_description =  (By.ID, "description")
    save = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
    def click_add_unit(self):
        unit_section = self.wait.until(
        EC.element_to_be_clickable(
            (self.add_unit_link)
        )
    )
        unit_section.click()

    def enter_name(self, name):
        name_unit =  self.wait.until(
        EC.visibility_of_element_located(
            (self.unit_name)
        )
            )
        name_unit.send_keys(name)

    def enter_code(self, code):
        code_name = self.wait.until(
        EC.visibility_of_element_located(
            (self.unit_code)
            )
        )
        code_name.send_keys(code)

    def enter_ratio(self, ratio):
        ratio_name = self.wait.until(
        EC.visibility_of_element_located(
            (self.unit_ratio)
            )
        )
        ratio_name.send_keys(ratio)

    def enter_description(self, description_val):
        description = self.wait.until(
        EC.visibility_of_element_located(
            (self.unit_description)
        )
    )
        description.send_keys(description_val)

    def click_save(self):
        save_button = self.wait.until(
                EC.element_to_be_clickable(
                    (self.save)
                )
            )
        save_button.click()

    def add_unit(self, name , code , ratio, description):
        self.click_add_unit()
        self.enter_name(name)
        self.enter_code(code)
        self.enter_ratio(ratio)
        self.enter_description(description)
        self.click_save()





    


        