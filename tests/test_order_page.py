import pytest
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestOrderPage:
    @pytest.mark.parametrize("order_button, name, surname, address, phone, logo, url ", [(BasePage.order_button_header_click, "Толик", "Бровнов", "Улица Марка, 22", "89085499657", OrderPage.click_yandex_logo, "ya.ru"), (BasePage.order_button_home_click, "Генадий", "Драков", "Улица Карла, 54", "+79013094965", OrderPage.click_scooter_logo, "qa-scooter.education-services.ru")])
    def test_full_order_success(self, driver, order_button, name, surname, address, phone, logo, url):
        base = BasePage(driver)
        order = OrderPage(driver)

        base.open_site()
        order_button(base)
        order.metro()
        order.order_fulfill(name, surname, address, phone)
        logo(order)
        current_url = order.get_current_url()

        assert url in current_url
