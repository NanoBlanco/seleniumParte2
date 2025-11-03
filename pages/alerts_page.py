from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class AlertsPage(BasePage):

    BTN_ALERTA = (By.ID, "btn-alerta")
    BTN_DELAY = (By.ID, "btn-mostrar-delay")
    MENSAJE_OCULTO = (By.ID, "mensaje-oculto")

    def manejar_alerta(self):
        self.click(self.BTN_ALERTA)
        self.accept_alert()

    def verificar_mensaje_delay(self):
        self.click(self.BTN_DELAY)
        # Esperar a que el mensaje deje de estar oculto
        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE_OCULTO)
        )
        return mensaje.text
