from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    name_field = (By.ID, "name")
    position_field = (By.ID, "itemPosition")
    category_control = (By.CSS_SELECTOR, ".react-select__control")
    description_field = (By.ID, "description")
    units_pricing_tab = (By.XPATH, "//a[normalize-space()='Units & Pricing']")
    unit_control = (By.CSS_SELECTOR, ".react-select__control.css-1nctvjd-control")
    dropdown_option = (By.CSS_SELECTOR, "div[role='option']")
    price_field = (By.XPATH, "//input[contains(@name, 'sellingPrice')]")
    save_button = (By.XPATH, "//button[normalize-space()='Save Product']")

    def __init__(self , driver , wait):
        self.driver = driver
        self.wait = wait

    def click_add(self):
        add_product = self.wait.until(
                EC.element_to_be_clickable((self.add_button))
                )
        add_product.click()

    def enter_name(self , name):
        add_name = self.wait.until(
            EC.visibility_of_element_located(
                (self.name_field)
            )
        )
        add_name.send_keys(name)

    def enter_product_position(self, product_position):

        position_field = self.wait.until(
            EC.visibility_of_element_located(self.position_field)
        )

        position_field.clear()
        position_field.send_keys(str(product_position))


    def select_category(self, product_category):
        category = self.wait.until(
            EC.element_to_be_clickable((self.category_control))
        )
        category.click()
        category_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-select__control input"))
        )
        category_input.send_keys(product_category)
        category_input.send_keys(Keys.ENTER)

    def enter_description(self, product_description):
        description = self.wait.until(
            EC.element_to_be_clickable((self.description_field))
            )
        description.send_keys(product_description)

    def click_units_pricing_tab(self):
        unit_tab = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Units & Pricing"))
            )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", unit_tab)
        
        unit_tab = self.wait.until(
                EC.element_to_be_clickable((self.units_pricing_tab))
            )
        try:
            unit_tab.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", unit_tab)

    
    def select_unit(self, product_unit):        
        unit_dropdown = self.wait.until(
                EC.element_to_be_clickable((self.unit_control))
            )
        unit_dropdown.click()
        
        unit_input = unit_dropdown.find_element(By.TAG_NAME, "input")
        unit_input.send_keys(product_unit)
        
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='option']")))
        unit_input.send_keys(Keys.ENTER)

    def enter_price(self, product_price):
        price = self.wait.until(
            EC.visibility_of_element_located((self.price_field))
        )
        price.send_keys(str(product_price))

    def click_save(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
        save_button.click()


    def add_product(self, product_category, product_name, product_price, product_unit, product_description,product_position):
        self.click_add()
        self.enter_name(product_name)
        self.enter_product_position(product_position)
        self.select_category(product_category)

        if product_description:
            self.enter_description(product_description)

        self.click_units_pricing_tab()
        self.select_unit(product_unit)
        self.enter_price(product_price)
        self.click_save()











