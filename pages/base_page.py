from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        # desplazarse al elemento antes de hacer clic
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception:
            # fallback en caso de superposición visual
            self.driver.execute_script("arguments[0].click();", element)

    def write(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def select_by_value(self, locator, value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.wait.until(EC.presence_of_element_located(locator)))
        select.select_by_value(value)

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))