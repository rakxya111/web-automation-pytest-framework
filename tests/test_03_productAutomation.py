import json
from pages.login_page import LoginPage
from pages.product_menu import ProductMenuPage
from utils.excel_utils import get_products_from_excel


with open("config/config.json") as f:
    config = json.load(f)


def test_product(driver, wait):

    # Login
    login_page = LoginPage(driver, wait)
    login_page.login(config["username"], config["password"])

    # Navigate to Product Page
    product_menu_page = ProductMenuPage(driver, wait)
    create_product_page = product_menu_page.go_to_productpage()

    # Read products from Excel
    products = get_products_from_excel(config["menu_list"])

    # Add products
    for product in products:
        create_product_page.add_product(
            product["category"],
            product["name"],
            product["price"],
            product["unit"],
            product["description"],
            product["position"],
        )