from pages.link_page import LinkPage

def test_click_enlace_google(go_to_base_page, driver):
    driver = go_to_base_page
    page = LinkPage(driver)
    url, title = page.click_enlace_google()
    assert "google.com" in url or "google" in title.lower()
