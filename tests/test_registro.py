from pages.registro_page import RegistroPage

def test_registro_usuario(driver):
    driver.get("https://web-form-selenium.netlify.app/")
    registro = RegistroPage(driver)
    texto = registro.registrar_usuario("usuario_test", "password123", "test@correo.com")
    assert "¡Registro exitoso para usuario_test!" in texto
