from .pages.login_page import LoginPage


def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page2 = LoginPage(browser, link)
    page2.open()
    page2.go_to_login_page()
    page2.should_be_login_page()
