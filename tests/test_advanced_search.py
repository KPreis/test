import allure
import pytest
from playwright.sync_api import Page
from pages.advanced_search_page import AdvancedSearchPage
from pages.vacancy_page import VacancyPage

SEARCH_URL = "https://hh.ru/search/vacancy/advanced"
PROFESSION = "Тестировщик"
REGION = "Москва"
SALARY = "100000"
CHECK_SALARY = "от 100 000 ₽"

@pytest.fixture
def advanced_search_page(page: Page):
  return AdvancedSearchPage(page)

@pytest.fixture
def results_search_page(page: Page):
  return VacancyPage(page)

@allure.feature("Advanced Search Page")
@allure.story("Advanced Search")
def test_basic_elements(advanced_search_page: AdvancedSearchPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
  
  with allure.step("Check basic elements"):
    assert advanced_search_page.profession_input.is_visible()
    assert advanced_search_page.region_input.is_visible()
    assert advanced_search_page.search_button.is_visible()

@allure.story("Check search by profession, region, salary and remote")
def test_combined_filters(advanced_search_page: AdvancedSearchPage, results_search_page: VacancyPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
 
  with allure.step("Fill profession, region, salary and remote"):
    advanced_search_page.fill_profession(PROFESSION)
    advanced_search_page.fill_region(REGION)
    advanced_search_page.fill_salary(SALARY)
    advanced_search_page.enable_remote_work()

  with allure.step("Click search button"):
    advanced_search_page.click_search()

  with allure.step("Check results page opened"):
    results_search_page.check_results_visible()
  
  with allure.step("Check filters results"):
    results_search_page.check_profession(PROFESSION)
    results_search_page.check_region(REGION)
    results_search_page.check_salary(CHECK_SALARY)
    results_search_page.check_on_enable_remote_work()