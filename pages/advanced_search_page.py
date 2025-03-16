from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class AdvancedSearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.title = page.locator("[data-qa='title']")

        self.profession_input = page.locator("[data-qa='vacancysearch__keywords-input']")
        #self.autofill_profession_input = page.get_by_text("ассистент HR") TODO: find locator
        #self.search_in_vacation_checkbox = page.locator("[data-qa=control-vacancysearch__search_field-item control-vacancysearch__search_field-item_name']")
        #self.search_in_company_name_checkbox = page.locator("[data-qa=control-vacancysearch__search_field-item control-vacancysearch__search_field-item_company_name']")
        #self.search_in_vacation_description_checkbox = page.locator("[data-qa=control-vacancysearch__search_field-item control-vacancysearch__search_field-item_description']")
        
        #self.profession_excluded_input = page.locator("[data-qa='vacancysearch__keywords-excluded-input']")

        #self.specialization_link = page.locator("[data-qa='resumesearch__profroles-switcher-text']")
        #self.specialization_modal_title = page.locator("#:r3:")
        #self.specialization_modal_input = page.locator("data-qa='tree-selector-search-input']")

        #self.specialization_company_link = page.locator("[data-qa='resumesearch__profroles-switcher-text']")
        #self.specialization_company_modal_title = page.locator("#:rp:")
        #self.specialization_company_modal_input = page.locator("[data-qa='tree-selector-search-input']")
        
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

    def check_results_visible(self):
        expect(self.page.locator("[data-qa='vacancy-serp__results']")).to_be_visible()
        