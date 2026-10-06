from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    ORDER_BUTTON_HOME = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]

    FAQ_QUESTION_TEMPLATE = [By.XPATH, "//div[@class='accordion__button' and text()='{question_text}']"]
    FAQ_ANSWER_TEMPLATE = [By.ID, "accordion__panel-{answer_id}"]
