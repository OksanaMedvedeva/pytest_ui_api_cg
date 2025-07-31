from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        # Пример использования By
        # в локаторе: locator = (By.ID, "some_id")
        return self.wait.until(
            EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)


# Пример использования класса BasePage
if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome()
    base_page = BasePage(driver)

    # Пример использования By для создания локатора
    locator = (By.ID, "example_id")
    base_page.find_element(locator)

    driver.quit()
