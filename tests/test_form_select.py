from conftest import driver
from pages.form_page import FormPage

def test_completar_formulario(go_to_base_page, driver):
    driver = go_to_base_page
    form_page = FormPage(driver)
    form_page.completar_formulario()
