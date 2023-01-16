import allure

from pages.form_page import FormPage
from allure_commons.types import AttachmentType



class TestFormPage:

    @allure.feature('Open pages')
    @allure.story('Open asos pages')
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://www.asos.com/')
        driver.delete_all_cookies()
        form_page.open()
        form_page.fill_fields_and_submit()
        driver.delete_all_cookies()


