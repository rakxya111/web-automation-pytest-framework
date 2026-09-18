from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

with open("config/config.json") as f:
    config = json.load(f)

class UnitMenuPage:

    def __init__(self, driver , wait):
        self.driver = driver
        self.wait = wait

    def go_to_unitpage(self):
        self.driver.get(config['unit_create_url'])
