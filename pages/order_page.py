import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Выбрать станцию метро на странице заказа")
    def metro(self):
        self.click(OrderPageLocators.METRO_FIELD)
        self.click(OrderPageLocators.METRO_STATION)

    @allure.step("Заполнить поля 'Имя', 'Фамилия', 'Адрес', 'Телефон' в форме заказа")
    def order_fulfill(self, name, surname, address, phone):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)
        self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Нажать на надпись 'Яндекс' в лого")
    def click_yandex_logo(self):
        self.click(OrderPageLocators.LOGO_YANDEX)
        self.switch_to_new_window()

    @allure.step("Нажать на надпись 'Самокат' в лого")
    def click_scooter_logo(self):
        self.click(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на кнопку 'Далее' на странице заказа")
    def click_next_order_button(self):
        self.click(OrderPageLocators.NEXT_ORDER_BUTTON)

    @allure.step("Выбрать дату доставки: 15-е число следующего месяца")
    def select_delivery_date(self):
        self.click(OrderPageLocators.WHEN_TO_GET_SCOOTER_FIELD)
        self.click(OrderPageLocators.NEXT_MONTH_BUTTON)
        self.click(OrderPageLocators.DAY_15)

    @allure.step("Выбрать срок аренды")
    def select_rent_time(self):
        self.click(OrderPageLocators.RENT_TIME_FIELD)
        self.click(OrderPageLocators.RENTAL_PERIOD_OPTION)

    @allure.step("Выбрать цвет самоката черный")
    def select_scooter_color(self):
        self.click(OrderPageLocators.COLOR_BLACK_CHECKBOX)

    @allure.step("Нажать кнопку завершения заказа")
    def click_finish_order_button(self):
        self.click(OrderPageLocators.FINISH_ORDER_BUTTON)

    @allure.step("Подтвердить завершение заказа")
    def click_confirm_finish_order_button(self):
        self.click(OrderPageLocators.CONFIRM_FINISH_ORDER_BUTTON)

    @allure.step("Проверить, что появилось сообщение 'Заказ оформлен'")
    def is_order_success_displayed(self):
        return self.is_element_present(OrderPageLocators.ORDER_SUCCESS_HEADER)
