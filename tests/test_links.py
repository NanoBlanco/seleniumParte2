from pages.link_page import LinkPage

def test_click_enlace_google(driver):
    driver.get("https://web-form-selenium.netlify.app/")
    page = LinkPage(driver)
    url, title = page.click_enlace_google()
    assert "google.com" in url or "google" in title.lower()
