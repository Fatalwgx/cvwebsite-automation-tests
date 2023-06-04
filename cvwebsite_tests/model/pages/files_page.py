
from .base_page import BasePage
from selene.support.shared import browser
from selene import have, be, command


class FilesPage(BasePage):
    def open(self):
        browser.open('/files')

    def pdf_file_header_present(self, pdf_name):
        pdf_header = browser.element(f'//h2[text()="{pdf_name}"]')
        command.js.scroll_into_view(pdf_header)
        pdf_header.should(be.visible)
        return self
