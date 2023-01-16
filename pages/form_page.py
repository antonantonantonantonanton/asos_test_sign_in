import time

import allure
from allure_commons.types import AttachmentType

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):

        first_name = 'Hello'
        last_name= 'World'
        email = 'hello@world.com'
        self.element_is_visible(locators.SIGN_IN).click()
        self.element_is_visible(locators.SIGN_IN_STEP_1).click()
        self.element_is_visible(locators.SIGN_IN_STEP_2).click()
        self.element_is_visible(locators.EMAIL).send_keys(email)
        self.element_is_visible(locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(locators.PASSWORD).send_keys('123456789//')
        self.element_is_visible(locators.DATE_OF_BIRTH).send_keys(15)
        self.element_is_visible(locators.MONTH_OF_BIRTH).send_keys('January')
        self.element_is_visible(locators.YEAR_OF_BIRTH).send_keys('1991')
        self.element_is_visible(locators.GENDER).click()
        self.element_is_visible(locators.SELLECT_ALL_CHECK_BUTTON).click()
        self.driver.execute_script('window.scrollTo(0, 1000)') #Скролит страницу вниз
        self.element_is_visible(locators.SUBMIT).click()
        with allure.step('Make screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        #self.driver.delete_all_cookies()
        time.sleep(10)

