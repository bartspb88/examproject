from .pages.prdct_page import ProductPage
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize('link',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket()
    product_page.solve_quiz_and_get_code()

    assert browser.find_element(By.XPATH, "//div[@id='messages']/div[1]"), "Сообщение о добавлении в корзину не найдено"

    product_name = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    product_name_text = product_name.text
    product_name_in_message = browser.find_element(By.XPATH,
                                                   "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    product_name_in_message_text = product_name_in_message.text
    assert product_name_text == product_name_in_message_text, 'Название товара в сообщении не совпадает с тем что добавляли'

    assert browser.find_element(By.XPATH, "//div[@id='messages']/div[3]"), "Сообщение о стоимости корзины не найдено"

    product_price = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    product_price_text = product_price.text
    product_price_in_basket = browser.find_element(By.XPATH,
                                                   "//div[@id='messages']/div[3]/div[@class='alertinner ']/p/strong")
    product_price_in_basket_text = product_price_in_basket.text
    assert product_price_text == product_price_in_basket_text, 'Стоимость в корзине не совпадает с тем что добавляли'
