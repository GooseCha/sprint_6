from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class OrderPage:
    URL = "https://qa-scooter.education-services.ru/"

    name_field = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    surname_field = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    address_field = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    metro_field = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    metro_station = [By.CLASS_NAME, "select-search__row"]
    phone_field = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    logo_yandex = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    logo_scooter = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    def __init__(self, driver):
        self.driver = driver

    def metro(self):
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(*self.metro_station).click()

    def order_fulfill(self, name, surname, address, phone):
        self.driver.find_element(*self.name_field).send_keys(f"{name}")
        self.driver.find_element(*self.surname_field).send_keys(f"{surname}")
        self.driver.find_element(*self.address_field).send_keys(f"{address}")
        self.driver.find_element(*self.phone_field).send_keys(f"{phone}")

    def click_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex).click()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)  # Про команду, чтобы узнать количество страниц в браузере и как на них перейти узнал у ИИшки
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

    def click_scooter_logo(self):
        self.driver.find_element(*self.logo_scooter).click()

    def get_current_url(self):
        return self.driver.current_url
