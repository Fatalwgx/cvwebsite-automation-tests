import allure
import pytest
from cvwebsite_tests.model import app
from selene.support.shared import browser


def test_from_homepage_go_to_slots_and_spin_succesfully():
    with allure.step("Openning Home page"):
        app.cv_page.open()

    with allure.step("Click projects navbar list"):
        app.cv_page.go_to_slots_page()

    with allure.step("Game field in initial position"):
        app.slots_page.empty_field_text_present()

    with allure.step("Making a spin"):
        app.slots_page.spin()

    with allure.step("Spin profits are present"):
        app.slots_page.profits_are_present()
        