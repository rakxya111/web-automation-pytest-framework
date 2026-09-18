import json
from pages.login_page import LoginPage
from pages.unit_page import UnitPage
from utils.excel_utils import get_unit_from_excel
from pages.unit_menu import UnitMenuPage


with open("config/config.json") as f:
    config = json.load(f)

def test_unit(driver, wait):

    login_page = LoginPage(driver, wait)
    unitMenu_page = UnitMenuPage(driver, wait)
    unit_page = UnitPage(driver, wait)

    login_page.login(config["username"], config["password"])

    # Navigate to Unit Page
    unitMenu_page.go_to_unitpage()

    # Read units from Excel
    units = get_unit_from_excel(config["unit_list"])

    for unit in units:
        unit_page.add_unit(
            unit['unit_name'],
            unit['unit_code'],
            unit['unit_ratio'],
            unit['unit_description'],
        )


        
