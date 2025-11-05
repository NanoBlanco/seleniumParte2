from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class RegistroPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    EMAIL = (By.ID, "email")
    BTN_SUBMIT = (By.ID, "submit-registro")
    RESULTADO = (By.ID, "resultado-registro")

    def registrar_usuario(self, username, password, email):
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.write(self.EMAIL, email)
        self.click(self.BTN_SUBMIT)
        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.RESULTADO)
        )
        return mensaje.text
