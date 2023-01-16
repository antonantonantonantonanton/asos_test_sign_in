from selenium.webdriver.common.by import By

class FormPageLocators():
    SIGN_IN = (By.CSS_SELECTOR, '#myAccountDropdown')
    SIGN_IN_STEP_1 = (By.CSS_SELECTOR, '[data-testid="signin-link"]')
    SIGN_IN_STEP_2 = (By.CSS_SELECTOR, '#new-to-asos-tab')

    EMAIL = (By.CSS_SELECTOR, '[data-st-field="id-register-email"]')
    FIRST_NAME = (By.CSS_SELECTOR, '[data-st-field="id-register-firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-st-field="id-register-lastName"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-st-field="id-register-password"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, '[aria-label="Date of birth Day"]')
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, '[aria-label="Date of birth Month"]')
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, '[aria-label="Date of birth Year"]')
    GENDER = (By.CSS_SELECTOR, '[class="radio qa-gender-male-label"]')
    SELLECT_ALL_CHECK_BUTTON = (By.CSS_SELECTOR, '#clear-all-checkbox-button')
    SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')



