import pytest
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestBasePage:
    @pytest.mark.parametrize(
        "question_text, answer_id, answer_text",
        [
            ("Сколько это стоит? И как оплатить?", "0", "Сутки — 400 рублей"),
            ("Хочу сразу несколько самокатов! Так можно?", "1", "Пока что у нас так"),
            ("Как рассчитывается время аренды?", "2", "Допустим, вы оформляете заказ"),
            ("Можно ли заказать самокат прямо на сегодня?", "3", "Только начиная с завтрашнего дня."),
            ("Можно ли продлить заказ или вернуть самокат раньше?", "4", "Пока что нет! "),
            ("Вы привозите зарядку вместе с самокатом?", "5", "Самокат приезжает к вам с полной зарядкой."),
            ("Можно ли отменить заказ?", "6", "Да, пока самокат не привезли."),
            ("Я жизу за МКАДом, привезёте?", "7", "Да, обязательно. Всем самокатов!"),
        ],
    )
    def test_faq_opens_success(self, driver, question_text, answer_id, answer_text):
        page = BasePage(driver)

        page.open_site()
        page.open_question(question_text)

        assert answer_text in page.get_answer_text(answer_id)
