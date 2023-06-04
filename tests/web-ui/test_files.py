import allure
import pytest
from cvwebsite_tests.model import app
from selene.support.shared import browser


@pytest.mark.parametrize(
    "header_name",
    [
        "Recommendation",
        "Python QA Automation Engineer",
        "Python Automation Course Certificate",
        "EF SET English Certificate 79/100 (C2 Proficient)",
        "My Resume",
        "Software QA Engineer",
    ],
)
def test_pdf_attachments_present(header_name):
    with allure.step("Openning File Attachments page"):
        app.file_page.open()

    with allure.step("Asserting headers presence"):
        app.file_page.pdf_file_header_present(pdf_name=header_name)
