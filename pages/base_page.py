from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент не найден или не кликабелен: {locator}")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(lambda d: d.current_url != "about:blank")

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
