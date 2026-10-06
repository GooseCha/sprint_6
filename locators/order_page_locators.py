from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    SURNAME_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    METRO_STATION = [By.CLASS_NAME, "select-search__row"]
    PHONE_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]

    LOGO_YANDEX = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    LOGO_SCOOTER = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    NEXT_ORDER_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    WHEN_TO_GET_SCOOTER_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]
    NEXT_MONTH_BUTTON = [By.CSS_SELECTOR, ".react-datepicker__navigation--next"]
    DAY_15 = [By.CSS_SELECTOR, ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"]

    RENT_TIME_FIELD = [By.XPATH, "//div[contains(text(), 'Срок аренды')]"]
    RENTAL_PERIOD_OPTION = [By.XPATH, "//div[contains(@class, 'Dropdown-option') and normalize-space()='трое суток']"]

    COLOR_BLACK_CHECKBOX = [By.ID, "black"]

    FINISH_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Button')]//button[text()='Заказать']"]
    CONFIRM_FINISH_ORDER_BUTTON = [By.XPATH, "//button[normalize-space()='Да']"]

    ORDER_SUCCESS_HEADER = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]"]
