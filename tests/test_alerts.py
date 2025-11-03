from pages.alerts_page import AlertsPage

def test_manejar_alerta(driver):
    driver.get("https://web-form-selenium.netlify.app/")
    page = AlertsPage(driver)
    page.manejar_alerta()

def test_verificar_mensaje_delay(driver):
    driver.get("https://web-form-selenium.netlify.app/")
    page = AlertsPage(driver)
    texto = page.verificar_mensaje_delay()
    assert "Éxito" in texto
