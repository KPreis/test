from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class AdvancedSearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.title = page.locator("[data-qa='title']")

        self.profession_input = page.locator("[data-qa='vacancysearch__keywords-input']")
        self.region_input = page.locator("[data-qa='advanced-search-region-add']")
        self.salary_input = page.locator("[data-qa='advanced-search-salary']")
        self.salary_only_checkbox = page.locator("[data-qa='control-vacancysearch__only-with-compensation']")
        self.search_button = page.locator("[data-qa='advanced-search-submit-button']")
        self.remote_work_checkbox = page.get_by_role("checkbox", name="Удалённо")


    def fill_profession(self, profession: str):
        self.profession_input.fill(profession)

    def fill_region(self, region: str):
        self.region_input.fill(region)

    def fill_salary(self, salary: str):
        self.salary_input.fill(salary)

    def enable_salary_only(self):
        self.salary_only_checkbox.click()

    def enable_remote_work(self):
        self.remote_work_checkbox.click()

    def click_search(self):
        print(self.search_button.is_visible())
        self.search_button.click()

    
        