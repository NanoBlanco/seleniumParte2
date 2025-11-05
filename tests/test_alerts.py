from pages.alerts_page import AlertsPage

def test_manejar_alerta(go_to_base_page, driver):
    driver = go_to_base_page
    page = AlertsPage(driver)
    page.manejar_alerta()

def test_verificar_mensaje_delay(go_to_base_page, driver):
    driver = go_to_base_page
    page = AlertsPage(driver)
    texto = page.verificar_mensaje_delay()
    assert "Éxito" in texto
