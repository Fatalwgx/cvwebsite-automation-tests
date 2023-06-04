
from .base_page import BasePage
from selene.support.shared import browser
from selene import have, be


class CvPage(BasePage):
    def __init__(self):
        self.cv_container = ...

    def open(self):
        browser.open('/')
        return self

    def cv_is_present(self):
        self.cv_container = browser.element('.rela-block .content-container').should(be.visible)
        return self

        
    

