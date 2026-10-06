import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Полное оформление заказа")
    @pytest.mark.parametrize("order_button, name, surname, address, phone", [(MainPage.click_order_header, "Толик", "Бровнов", "Улица Марка, 22", "89085499657"), (MainPage.click_order_home, "Генадий", "Драков", "Улица Карла, 54", "+79013094965")])
    def test_full_order_success(self, driver, order_button, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_site()
        order_button(main_page)
        order_page.metro()
        order_page.order_fulfill(name, surname, address, phone)
        order_page.click_next_order_button()
        order_page.select_delivery_date()
        order_page.select_rent_time()
        order_page.select_scooter_color()
        order_page.click_finish_order_button()
        order_page.click_confirm_finish_order_button()

        assert order_page.is_order_success_displayed(), "Сообщение 'Заказ оформлен' не появилось"

    @allure.title("Редирект по кнопке 'Яндекс'")
    def test_yandex_redirect_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_site()
        order_page.click_yandex_logo()
        current_url = order_page.get_current_url()

        assert "ya.ru" in current_url

    @allure.title("Редирект по кнопке 'Самокат'")
    def test_scooter_redirect_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_site()
        main_page.click_order_header()
        order_page.click_scooter_logo()
        current_url = order_page.get_current_url()

        assert "qa-scooter.education-services.ru" in current_url
