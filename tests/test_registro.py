from pages.registro_page import RegistroPage

def test_registro_usuario(go_to_base_page, driver):
    # driver.get("https://web-form-selenium.netlify.app/")
    driver = go_to_base_page
    registro = RegistroPage(driver)
    texto = registro.registrar_usuario("usuario_test", "password123", "test@correo.com")
    assert "¡Registro exitoso para usuario_test!" in texto
