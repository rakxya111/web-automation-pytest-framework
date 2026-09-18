import json
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.category_page import CatgoryPage
from utils.excel_utils import get_categories_from_excel


test_data_path = "test_data/test_data.json"

with open("config/config.json") as f:
    config = json.load(f)

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

# Category automation

@pytest.mark.parametrize("test_list_item", test_list)
def test_category(driver, wait , test_list_item):
    
    login_page = LoginPage(driver, wait)
    # dashboard_page = DashboardPage(driver, wait)
    # category_page = CatgoryPage(driver, wait)

    # LOGIN
    login_page.login(test_list_item['userEmail'],test_list_item['userPassword'])
   
    # NAVIGATION TO THE CATEGORY PAGE
    dashboard_page = DashboardPage(driver, wait)
    category_page = dashboard_page.go_to_category()

    # Read categories from Excel
    categories = get_categories_from_excel(config['category_list'])

    # Add categories automation
    for category_name in categories:
        category_page.add_category(category_name)




