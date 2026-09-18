# 🧪 Web Automation Pytest Framework

A Python-based web automation framework built with **Selenium WebDriver and Pytest**, following the **Page Object Model (POM)** design pattern and supporting **Excel-driven data-driven testing**.

The framework automates key workflows of a web-based inventory management application, including **Unit, Category, and Product creation**.

---

## 🔍 Table of Contents

* [Demo](#-demo)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Automation Flow](#-automation-flow)
* [Data-Driven Testing](#-data-driven-testing)
* [Page Object Model](#-page-object-model)
* [Folder Structure](#-folder-structure)
* [Test Coverage](#-test-coverage)
* [Configuration](#-configuration)
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

> Video demonstration of the automated Unit, Category, and Product creation workflows will be added here.

https://github.com/user-attachments/assets/5c3c4f60-ec5b-4302-a3bf-dfd6a5d692c4
<!-- Video/GIF will be added here -->

---

## ✨ Features

* 🌐 Web UI automation using Selenium WebDriver
* 🧪 Test execution using Pytest
* 🧩 Page Object Model (POM) architecture
* 📊 Excel-based data-driven testing
* 🔄 Pytest parameterization
* 🌍 Chrome and Firefox browser support
* ⚙️ Centralized configuration using JSON
* ⏱️ Explicit waits using `WebDriverWait`
* 📸 Automatic screenshots on test failure
* 📋 HTML test reports using `pytest-html`
* ♻️ Reusable Pytest fixtures
* 📁 Separate page objects, test cases, utilities, and test data
* 🔐 Sensitive credentials excluded from the public repository

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.46.0-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.1.1-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.5-2F6B3F?style=for-the-badge)
![Python](https://img.shields.io/badge/Data--Driven-Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 🔄 Automation Flow

The automation is organized into three major workflows:

```text
                    Login
                      │
                      ▼
              ┌───────────────┐
              │ Unit Creation │
              └───────┬───────┘
                      │
                      ▼
            ┌───────────────────┐
            │ Category Creation │
            └─────────┬─────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Product Creation│
             └─────────────────┘
