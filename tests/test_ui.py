import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BASE_URL, PHONE_NUMBER


@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


@allure.feature("UI Тесты")
@allure.story("Проверка ввода номера телефона")
def test_phone_number_input(driver):
    # Открытие веб-страницы
    with allure.step("Открытие веб-страницы"):
        driver.get(BASE_URL)

    # Поиск поля для ввода номера телефона и ввод номера
    with allure.step("Ввод номера телефона"):
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='tel']")
            )
        )
        phone_input.send_keys(PHONE_NUMBER)

    # Проверка, что номер телефона введен корректно
    with allure.step("Проверка ввода номера телефона"):
        assert phone_input.get_attribute("value") == PHONE_NUMBER


@allure.feature("UI Тесты")
@allure.story("Проверка кнопки 'Получить код'")
def test_get_code_button(driver):
    # Открытие веб-страницы
    with allure.step("Открытие веб-страницы"):
        driver.get(BASE_URL)

    # Поиск поля для ввода номера телефона и ввод номера
    with allure.step("Ввод номера телефона"):
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[type='tel']")
            )
        )
        phone_input.send_keys(PHONE_NUMBER)

    # Поиск и нажатие кнопки "Получить код"
    with allure.step("Нажатие кнопки 'Получить код'"):
        get_code_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        get_code_button.click()

    # Проверка сообщения об отправке SMS
    with allure.step("Проверка сообщения об отправке SMS"):
        sms_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains("
                           "text(), 'Отправили СМС с кодом на номер')]")
            )
        )
        assert "Отправили СМС с кодом на номер" in sms_message.text


@allure.feature("UI Тесты")
@allure.story("Проверка ссылки 'Запросить новый код'")
def test_request_new_code_link(driver):
    # Открытие веб-страницы
    with allure.step("Открытие веб-страницы"):
        driver.get(BASE_URL)

    # Поиск поля для ввода номера телефона и ввод номера
    with allure.step("Ввод номера телефона"):
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='tel']")
            )
        )
        phone_input.send_keys(PHONE_NUMBER)

    # Поиск и нажатие кнопки "Получить код"
    with allure.step("Нажатие кнопки 'Получить код'"):
        get_code_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        get_code_button.click()

    # Проверка таймера обратного отсчета
    with allure.step("Проверка таймера обратного отсчета"):
        timer_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains("
                           "text(), 'Запросить новый код можно через')]")
            )
        )
        assert "Запросить новый код можно через" in timer_message.text

    # Поиск и нажатие ссылки "Запросить новый код"
    with allure.step("Нажатие ссылки 'Запросить новый код'"):
        request_new_code_link = driver.find_element(
            By.LINK_TEXT, "Запросить новый код")
        request_new_code_link.click()

    # Проверка нового сообщения об отправке SMS
    with allure.step("Проверка нового сообщения об отправке SMS"):
        new_sms_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH, "//div[contains(text(), 'Отправили СМС "
                              "с кодом на номер')]")
            )
        )
        assert "Отправили СМС с кодом на номер" in new_sms_message.text


@allure.feature("UI Тесты")
@allure.story("Проверка кнопки 'Продолжить'")
def test_continue_button(driver):
    # Открытие веб-страницы
    with allure.step("Открытие веб-страницы"):
        driver.get(BASE_URL)

    # Поиск поля для ввода номера телефона и ввод номера
    with allure.step("Ввод номера телефона"):
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[type='tel']"))
        )
        phone_input.send_keys(PHONE_NUMBER)

    # Поиск и нажатие кнопки "Получить код"
    with allure.step("Нажатие кнопки 'Получить код'"):
        get_code_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        get_code_button.click()

    # Проверка состояния кнопки "Продолжить"
    with allure.step("Проверка состояния кнопки 'Продолжить'"):
        continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "button.continue-button"))
        )
        assert continue_button.is_enabled()


@allure.feature("UI Тесты")
@allure.story("Проверка таймера после повторного запроса кода")
def test_timer_display_after_requesting_new_code(driver):
    # Открытие веб-страницы
    with allure.step("Открытие веб-страницы"):
        driver.get(BASE_URL)

    # Поиск поля для ввода номера телефона и ввод номера
    with allure.step("Ввод номера телефона"):
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[type='tel']"))
        )
        phone_input.send_keys(PHONE_NUMBER)

    # Поиск и нажатие кнопки "Получить код"
    with allure.step("Нажатие кнопки 'Получить код'"):
        get_code_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        get_code_button.click()

    # Поиск и нажатие ссылки "Запросить новый код"
    with allure.step("Нажатие ссылки 'Запросить новый код'"):
        request_new_code_link = driver.find_element(
            By.LINK_TEXT, "Запросить новый код")
        request_new_code_link.click()

    # Проверка сброса таймера
    with allure.step("Проверка сброса таймера"):
        timer_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//div[contains(text(), 'Запросить новый"
                          " код можно через')]"))
        )
        assert "Запросить новый код можно через" in timer_message.text
