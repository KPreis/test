from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)

    def wait_for_element(self, locator: str):
        self.page.wait_for_selector(locator)