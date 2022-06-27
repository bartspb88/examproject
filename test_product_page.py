from .pages.prdct_page import ProductPage
from selenium.webdriver.common.by import By


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket()
    product_page.solve_quiz_and_get_code()


def test_guest_message_about_add_product_to_basket(browser):
    assert browser.find_element(By.XPATH, "//div[@id='messages']/div[1]")


def test_guest_product_name_same_that_add(browser):
    product_name = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    product_name_text = product_name.text
    product_name_in_message = browser.find_element(By.XPATH,
                                                   "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    product_name_in_message_text = product_name_in_message.text
    assert product_name_text == product_name_in_message_text, 'Название добавленного товара не совпадает с тем что добавляли'


def test_guest_message_about_basket_cost(browser):
    assert browser.find_element(By.XPATH, "//div[@id='messages']/div[3]")


def test_guest_basket_cost_same_product_price(browser):
    product_price = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    product_price_text = product_price.text
    product_price_in_basket = browser.find_element(By.XPATH,
                                                   "//div[@id='messages']/div[3]/div[@class='alertinner ']/p/strong")
    product_price_in_basket_text = product_price_in_basket.text
    assert product_price_text == product_price_in_basket_text, 'Название добавленного товара не совпадает с тем что добавляли'
