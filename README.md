# 🧪 Web Automation Pytest Framework

A Python-based web automation framework built with **Selenium WebDriver and Pytest**, following the **Page Object Model (POM)** design pattern.

The framework automates key workflows of a web-based inventory management application, including **Unit, Category, and Product creation**, with support for **Excel-driven test data, reusable fixtures, centralized configuration, explicit waits, failure screenshots, and HTML test reports**.

---

## 🔍 Table of Contents

* [Demo](#-demo)
* [Features](#-features)
* [Tech Stack](#️-tech-stack)
* [Automation Flow](#-automation-flow)
* [Framework Architecture](#️-framework-architecture)
* [Data-Driven Testing](#-data-driven-testing)
* [Page Object Model](#-page-object-model)
* [Folder Structure](#-folder-structure)
* [Test Coverage](#-test-coverage)
* [Configuration](#️-configuration)
* [Installation](#-installation)
* [Running the Tests](#-running-the-tests)
* [Test Reports](#-test-reports)
* [Failure Screenshots](#-failure-screenshots)
* [Future Improvements](#-future-improvements)
* [License](#-license)
* [Author](#-author)

---

## 🚀 Demo

📽️ **Automation Demo Video**

A short demonstration of the framework executing the automated Unit, Category, and Product creation workflows.

https://github.com/user-attachments/assets/5c3c4f60-ec5b-4302-a3bf-dfd6a5d692c4

---

## ✨ Features

* 🌐 Web UI automation using **Selenium WebDriver**
* 🧪 Test execution using **Pytest**
* 🧩 **Page Object Model (POM)** architecture
* 📊 **Excel-based data-driven testing**
* 🔄 Pytest fixtures and reusable test components
* 🌍 Chrome and Firefox browser support
* ⚙️ Centralized configuration using **JSON**
* ⏱️ Explicit waits using `WebDriverWait`
* 📸 Automatic screenshots on test failure
* 📋 HTML test reports using `pytest-html`
* 📁 Separation of test cases, page objects, utilities, and test data
* 🔐 Test credentials kept separate from the public repository
* ♻️ Reusable page-level methods for common application workflows

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.46.0-43B02A?style=for-the-badge\&logo=selenium\&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.1.1-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.5-2F6B3F?style=for-the-badge)
![Excel](https://img.shields.io/badge/Excel-Data--Driven-217346?style=for-the-badge\&logo=microsoftexcel\&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 🔄 Automation Flow

The framework automates the following major workflows:

```text
                         Login
                           │
                           ▼
                  ┌─────────────────┐
                  │  Unit Creation  │
                  │   Excel Data    │
                  └────────┬────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Category Creation  │
                │    Excel Data       │
                └──────────┬──────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Product Creation │
                 │   Excel Data     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Test Execution   │
                 └────────┬─────────┘
                          │
                  ┌───────┴────────┐
                  ▼                ▼
            HTML Report      Failure Screenshot
```

---

## 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** architecture to separate test logic from page-specific UI interactions.

```text
                    Test Cases
                        │
                        ▼
                  Page Objects
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      Login Page     Unit Page    Category Page
                                      │
                                      ▼
                                 Product Page
                        │
                        ▼
                    Utilities
              ┌─────────┴─────────┐
              ▼                   ▼
        Excel Utilities      Configuration
              │
              ▼
          Test Data
       ┌──────┴──────┐
       ▼             ▼
     Excel          JSON
```

This structure helps keep the framework **organized, reusable, and maintainable** as more automated workflows are added.

---

## 📊 Data-Driven Testing

The framework uses **Excel files as test data sources** for workflows that require multiple input records.

Excel data is read using **OpenPyXL** and passed to the relevant test/page methods.

Example:

```text
Excel Test Data
      │
      ▼
Excel Utility
      │
      ▼
Python Dictionary
      │
      ▼
Pytest Test
      │
      ▼
Page Object Methods
      │
      ▼
Web Application
```

This approach allows test data to be modified without changing the core automation logic.

---

## 🧩 Page Object Model

Each major application workflow is represented by a dedicated page object.

### Example Page Objects

| Page Object     | Responsibility               |
| --------------- | ---------------------------- |
| `LoginPage`     | Handles application login    |
| `UnitPage`      | Handles unit creation        |
| `CategoryPage`  | Handles category creation    |
| `ProductPage`   | Handles product creation     |
| `DashboardPage` | Handles dashboard navigation |

Page objects contain **locators and reusable UI interaction methods**, while test files focus on **test execution and validation**.

This separation makes the automation easier to maintain when the application's UI changes.

---

## 📁 Folder Structure

```text
inventory-management-automation/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── unit_page.py
│   ├── category_page.py
│   └── product_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_unit.py
│   ├── test_category.py
│   └── test_product.py
│
├── utils/
│   ├── excel_utils.py
│   └── category_attribute_map.py
│
├── test_data/
│   ├── units.xlsx
│   ├── categories.xlsx
│   └── products.xlsx
│
├── config/
│   └── config.json
│
├── reports/
│   └── report.html
│
├── screenshots/
│   └── ...
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

> The exact filenames and folders may vary depending on the current implementation of the project.

---

## 🧪 Test Coverage

The current framework covers key inventory-management workflows.

| Module           | Workflow           | Test Data     | Automation |
| ---------------- | ------------------ | ------------- | ---------- |
| Login            | User login         | Configuration | ✅          |
| Unit             | Create unit        | Excel         | ✅          |
| Category         | Create category    | Excel         | ✅          |
| Product          | Create product     | Excel         | ✅          |
| Browser          | Chrome execution   | Configuration | ✅          |
| Browser          | Firefox execution  | Configuration | ✅          |
| Reporting        | HTML test report   | Pytest        | ✅          |
| Failure Handling | Screenshot capture | Pytest hook   | ✅          |

### Product Workflow

The Product workflow supports application-specific product information and dynamic attributes, including fields that can change depending on the selected product category.

The framework uses an attribute mapping approach to associate test data with the corresponding UI attributes.

---

## ⚙️ Configuration

Application and execution settings are centralized using JSON configuration.

Example:

```json
{
    "browser": "chrome",
    "url": "https://example.com",
    "timeout": 15
}
```

Configuration can be used for values such as:

* Browser
* Application URL
* Explicit wait timeout
* Other environment-independent settings

Keeping configuration separate from the test logic makes it easier to change execution settings without modifying the test cases.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/inventory-management-automation.git
```

### 2. Navigate to the Project

```bash
cd inventory-management-automation
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

### Run All Tests

```bash
pytest
```

### Run Tests with HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Run a Specific Test File

```bash
pytest tests/test_product.py
```

### Run with a Specific Browser

If browser selection is configured through the Pytest command line:

```bash
pytest --browser_name chrome
```

or:

```bash
pytest --browser_name firefox
```

---

## 📋 Test Reports

The framework uses **pytest-html** to generate HTML test execution reports.

Example:

```text
reports/
└── report.html
```

The report provides information such as:

* Test execution status
* Passed tests
* Failed tests
* Test duration
* Environment information
* Failure details

---

## 📸 Failure Screenshots

Screenshots are automatically captured when a test fails.

Example:

```text
screenshots/
├── test_create_unit_failure.png
├── test_create_category_failure.png
└── test_create_product_failure.png
```

This makes it easier to identify the application's state at the time of failure and helps with debugging failed automation tests.

---

## 🔐 Security

Sensitive credentials and environment-specific information are not intended to be committed to the public repository.

The project uses configuration/separate credential handling so that sensitive information can remain outside the publicly shared source code.

> Before publishing the repository, verify that passwords, tokens, API keys, private URLs, and other sensitive information are excluded through `.gitignore` and repository configuration.

---

## 🔮 Future Improvements

Planned improvements for the framework include:

* 🔄 CI/CD integration using Jenkins
* 🌐 Cross-browser test execution improvements
* ⚡ Parallel test execution
* 🔌 API test integration
* 🗄️ Database validation
* 📊 Enhanced test reporting
* 🐳 Docker-based test execution
* 🧪 Expanded negative and edge-case test coverage

---

## 📄 License

This project is intended for **learning, portfolio, and demonstration purposes**.

---

## 👩‍💻 Author

**Rakshya Bhuju**

QA Automation Enthusiast | Python | Selenium | Pytest

🔗 GitHub: [github.com/rakxya111](https://github.com/rakxya111)

---

⭐ If you find this project useful, feel free to explore the repository and the automation implementation.
