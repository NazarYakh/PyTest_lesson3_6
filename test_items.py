import time
from selenium.common.exceptions import NoSuchElementException


class TestsBasketButton(object):

    def test_find_basket_button(self, browser):

        link: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        browser.get(link)

        time.sleep(2)

        try:
            browser.find_element_by_css_selector("button.btn-add-to-basket")
            search_button = True
        except NoSuchElementException:
            search_button = False

        assert search_button, "Basket button is not found"
