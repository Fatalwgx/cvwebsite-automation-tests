from .base_page import BasePage
from selene.support.shared import browser
from selene import have, be, command



class SlotsPage(BasePage):
    def open(self):
        browser.open("/projects/slots")
        return self

    def spin(self):
        browser.element('.btn1').click()
        return self

    def empty_field_text_present(self):
        browser.element('//p[text()="Press \'Spin\' to start"]').should(be.visible)
        return self
    
    def profits_are_present(self):
        browser.element('.winnings').with_(timeout=6).should(be.visible)
        return self

