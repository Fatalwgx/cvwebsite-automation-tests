
from selene.support.shared import browser
from selene import have, be


class BasePage:
    def __init__(self):
        ...
        
    def navbar_tab_highlited(self, tab_name: str):
        browser.element('.active').should(have.text(tab_name))
        return self

    def navbar_tab_present(self, tab_name: str):
        browser.element('//a[@href="/files/cv"]').should(have.text(tab_name))
        return self