from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormPage(BasePage):

    # Locators
    DROPDOWN = (By.ID, "opcion-dropdown")
    RADIO_OPCION_B = (By.ID, "radio-opcion-b")
    CHECK_TERMINOS = (By.ID, "check-terminos")
    CHECK_NEWSLETTER = (By.ID, "check-newsletter")
    COMENTARIOS = (By.ID, "comentarios")

    def completar_formulario(self):
        # seleccionar item 2 del select (value="2")
        self.select_by_value(self.DROPDOWN, "op2")

        # seleccionar el radio button con id radio-opcion-b
        self.click(self.RADIO_OPCION_B)

        # marcar los dos checkboxes
        self.click(self.CHECK_TERMINOS)
        self.click(self.CHECK_NEWSLETTER)

        # escribir en el cuadro de comentarios
        self.write(self.COMENTARIOS, "Este es un comentario de prueba.")
