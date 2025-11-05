# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    """Crea una única instancia de navegador para toda la sesión de pruebas."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # opciones adicionales si quieres acelerar: headless, disable-gpu, etc.

    service = Service()  # Usa el ChromeDriver del PATH
    driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(5)

    yield driver  # Aquí se entrega el navegador a las pruebas

    driver.quit()  # Se cierra al final de TODAS las pruebas

@pytest.fixture(scope="module")
def go_to_base_page(driver):
    base_url = "https://web-form-selenium.netlify.app/"
    driver.get(base_url)
    return driver