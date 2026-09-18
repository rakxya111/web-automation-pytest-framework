import os
import json
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


with open("config/config.json") as f:
    config = json.load(f)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Run tests on selected browser"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.get(config['url'])

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, config['timeout'])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir,
                report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            )
            driver.get_screenshot_as_file(file_name)

            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, mime_type="image/png"))

    report.extras = extra