# 🚀 Описание проекта  
Автотесты на Python для API (httpx) и UI (Playwright) 

Страница проекта: https://taiga.io/  
Allure-Report: https://zomlik.github.io/project-autotests/

## 🛠 Технологии
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-00A98F?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6A00?style=for-the-badge&logo=allure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## 🧪 Переменные окружения
Проект использует переменные окружения из файла `.env`. Создайте его на основе примера:
   ```bash
    cp .env.example .env
   ```
Затем отредактируйте `.env` файл, указав свои значения:
```ini
# .env.example
HTTP_CLIENT.BASE_URL = "http://localhost:9000/api/v1"
HTTP_CLIENT.TIMEOUT = 100 

PLAYWRIGHT.BASE_URL = "http://localhost:9000"
PLAYWRIGHT.HEADLESS = False 
```
## ⚙️ Установка
1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/zomlik/project-autotests.git
   ```
2. Создать виртуальное окружение:  
   Linux/MacOs
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```  
   Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Установить браузеры:
   ```bash
   playwright install
   ```
5. Запуск тестов:
    ```bash
   pytest --alluredir allure-results
   ```
   
## 📁 Структура проекта
```
project-autotest/
├──.github/                 # GitHub Workflows
├── api/                    # Логика для API автотестов
├── components/             # PageComponents
├── elements/               # PageFactory
├── fixtures/               # Фикстуры pytest
├── locators/               # Локаторы элементов (XPath/CSS-селекторы)
├── models/                 # Pydantic модели
├── pages/                  # Page Objects
├── tests/                  # Тестовые сценарии
│   ├── api/                # API-тесты
│   ├── ui/                 # UI-тесты
├── utils/                  # Вспомогательные утилиты
├── .env.example            # Пример файла окружения
├── config.py               # Настройки проека Pydantic-settings
├── conftest.py             # Настройки pytest
├── pytest.ini              # Конфиг pytest
├── requirements.txt        # Зависимости Python
```
