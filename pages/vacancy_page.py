from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class VacancyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.profession_input = page.locator("[data-qa='search-input']")
        self.title = page.locator("[data-qa='title']")
        self.search_button = page.locator("[data-qa='search-button']")

        self.currency_switcher = page.locator("[data-qa='link-icon-external']")
        self.currency_rub = page.get_by_role("button", name="₽")
        self.currency_eur = page.get_by_role("button", name="€")
        self.currency_usd = page.get_by_role("button", name="$") 

        self.custom_salary_radio_btn = page.get_by_role("radio", name="Своя зарплата")
        self.custon_salary_input = page.locator("[data-qa='novafilters-custom-compensation']")

        self.salary_only_checkbox = page.get_by_role("checkbox", name="Указан доход")
        self.remote_work_checkbox = page.get_by_role("checkbox", name="Удалённо")

    def check_profession(self, profession: str):
        expect(self.profession_input).to_have_value(profession)

    def check_region(self, region: str):
        expect(self.page.get_by_role("checkbox", name=region)).to_be_checked()
        
    def check_salary(self, salary: str):
        if salary == "Не имеет значения":
            income_group = self.page.get_by_role("group").filter(has_text="Уровень дохода")
            target_radio = income_group.get_by_role("radio", name=salary)
            expect(target_radio).to_be_checked()
        else:
            expect(self.page.get_by_role("radio", name=salary)).to_be_checked()

    def check_on_enable_remote_work(self):
        expect(self.remote_work_checkbox).to_be_checked()

    def enable_salary_only(self):
        self.salary_only_checkbox.click()

    def check_on_enable_salary_only(self):
        self.salary_only_checkbox.is_checked()
        expect(self.salary_only_checkbox).to_be_checked()

    def fill_custom_salary(self, salary: str):
        self.custom_salary_radio_btn.click()
        self.custon_salary_input.fill(salary)
        self.custon_salary_input.press("Enter")
    
    def switch_currency(self, currency: str):
        if currency == "RUB":
            self.currency_switcher.click()
            self.currency_rub.click()
        elif currency == "EUR":
            self.currency_switcher.click()
            self.currency_eur.click()
        elif currency == "USD":
            self.currency_switcher.click()
            self.currency_usd.click()

    def click_search(self):
        self.search_button.click()

    def check_results_visible(self):
        expect(self.page.locator("[data-qa='vacancy-serp__results']")).to_be_visible()