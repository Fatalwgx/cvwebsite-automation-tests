
import allure
from cvwebsite_tests.model import app
from selene.support.shared import browser


def test_cv_header_is_present():
    with allure.step('Opening CV page'):
        app.cv_page.open()

    with allure.step():
        app.cv_page.cv_is_present()
