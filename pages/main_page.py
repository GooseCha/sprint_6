import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "https://qa-scooter.education-services.ru/"

    @allure.step("Открыть главную страницу сайта")
    def open_site(self):
        self.open(self.URL)

    @allure.step("Нажать на кнопку 'Заказать' в хедере")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать на кнопку 'Заказать' на главной странице")
    def click_order_home(self):
        self.click(MainPageLocators.ORDER_BUTTON_HOME)

    @allure.step("Открыть вопрос FAQ: {question_text}")
    def open_question(self, question_text):
        locator = (
            MainPageLocators.FAQ_QUESTION_TEMPLATE[0],
            MainPageLocators.FAQ_QUESTION_TEMPLATE[1].format(question_text=question_text),
        )
        self.click(locator)

    @allure.step("Получить текст ответа с id={answer_id}")
    def get_answer_text(self, answer_id):
        locator = (
            MainPageLocators.FAQ_ANSWER_TEMPLATE[0],
            MainPageLocators.FAQ_ANSWER_TEMPLATE[1].format(answer_id=answer_id),
        )
        return self.get_text(locator)
