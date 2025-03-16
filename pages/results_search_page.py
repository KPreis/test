from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ResultsSearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.profession_input = page.get_by_role("textbox", name="Поиск по вакансиям")
        
        self.salary_100K = page.get_by_role("radio", name="от 100 000 ₽")
        self.salary_only_checkbox = page.locator("[data-qa='control-vacancysearch__only-with-compensation']")
        self.remote_work_checkbox = page.get_by_role("checkbox", name="Удалённо")

    def check_profession(self, profession: str):
        expect(self.profession_input).to_have_value(profession)

    def check_region(self, region: str):
        expect(self.page.get_by_role("checkbox", name=region)).to_be_checked()
        
    def check_salary(self, salary: str):
        expect(self.page.get_by_role("radio", name=salary)).to_be_checked()

    def check_on_enable_remote_work(self):
        expect(self.remote_work_checkbox).to_be_checked()

    def click_search(self):
        print(self.search_button.is_visible())
        self.search_button.click()

    def check_results_visible(self):
        expect(self.page.locator("[data-qa='vacancy-serp__results']")).to_be_visible()