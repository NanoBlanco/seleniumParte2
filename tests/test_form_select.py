from pages.form_page import FormPage

def test_completar_formulario(driver):
    driver.get("https://web-form-selenium.netlify.app/")
    form_page = FormPage(driver)
    form_page.completar_formulario()
