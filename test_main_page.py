from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CardPage
import pytest

def go_to_login_page(browser):
    link = browser.find_element_by_css_selector('#login_link')
    link.click()

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

        
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = CardPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
