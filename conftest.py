import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()