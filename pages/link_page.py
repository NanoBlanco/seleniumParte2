from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LinkPage(BasePage):
    LINK_GOOGLE = (By.ID, "link-google")

    def click_enlace_google(self):
        original_tab = self.driver.current_window_handle
        self.click(self.LINK_GOOGLE)

        # Esperar un momento a que se abra la nueva pestaña
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # Cambiar al nuevo tab
        new_tab = [tab for tab in self.driver.window_handles if tab != original_tab][0]
        self.driver.switch_to.window(new_tab)

        # Esperar a que cargue la página de destino
        time.sleep(2)
        current_url = self.driver.current_url
        title = self.driver.title

        # Cerrar la pestaña nueva y volver a la original
        self.driver.close()
        self.driver.switch_to.window(original_tab)

        return current_url, title
