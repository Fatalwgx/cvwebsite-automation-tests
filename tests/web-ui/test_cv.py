
import allure
from cvwebsite_tests.model import app
from selene.support.shared import browser


def test_cv_header_is_present(setup_browser):
    with allure.step('Opening CV page'):
        app.cv_page.open()

    with allure.step('Asserting cv presence'):
        app.cv_page.cv_is_present()


def test_navbar_tab_is_highlighted(setup_browser):
    with allure.step('Openning CV page'):
        app.cv_page.open()

    with allure.step('Asserting navbar Home tab highlight'):
        app.cv_page.navbar_tab_highlited('Home')


def test_download_cv_tav_present(setup_browser):
    with allure.step('Openning CV page'):
        app.cv_page.open()

    with allure.step('Asserting navbar Download CV presence'):
        app.cv_page.navbar_tab_highlited('Home')