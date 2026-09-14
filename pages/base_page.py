from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    URL = "https://qa-scooter.education-services.ru/"

    order_button_header = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    order_button_home = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]

    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get(self.URL)

    def open_question(self, question_text):
        locator = (By.XPATH, f"//div[@class='accordion__button' and text()='{question_text}']")
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, answer_id):
        locator = (By.ID, f"accordion__panel-{answer_id}")
        answer = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return answer.text

    def order_button_header_click(self):
        self.driver.find_element(*self.order_button_header).click()

    def order_button_home_click(self):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.driver.find_element(*self.order_button_home))
        self.driver.find_element(*self.order_button_home).click()
