from .main_page import MainPage
from .locators import ProductPageLocators


class ProductPage(MainPage):
    def should_be_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
