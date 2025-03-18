import allure
import pytest
from playwright.sync_api import Page
from pages.advanced_search_page import AdvancedSearchPage
from pages.vacancy_page import VacancyPage

SEARCH_URL = "https://hh.ru/search/vacancy/advanced"
SALARY_LESS_0K = "-10000"
CHECK_SALARY_10K = "от 10 000 ₽"
SALARY_90K = "90000"
CHECK_SALARY_90K = "от 90 000 ₽"
SALARY_1M = "1000000"
CHECK_SALARY_1M = "от 1 000 000 ₽"



@pytest.fixture
def advanced_search_page(page: Page):
  return AdvancedSearchPage(page)

@pytest.fixture
def vacancy_page(page: Page):
  return VacancyPage(page)

@allure.feature("Advanced Search Page")
@allure.story("Advanced Search - Salary Filter")
def test_basic_elements(advanced_search_page: AdvancedSearchPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
  
  with allure.step("Check basic elements"):
    assert advanced_search_page.profession_input.is_visible()
    assert advanced_search_page.region_input.is_visible()
    assert advanced_search_page.search_button.is_visible()

@allure.story("Advanced Search - Check search by salary only")
def test_salary_filter(advanced_search_page: AdvancedSearchPage, vacancy_page: VacancyPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
  
  with allure.step("Fill salary filter"):
    advanced_search_page.fill_salary(SALARY_90K)
  
  with allure.step("Enable salary only"):
    advanced_search_page.enable_salary_only()
  
  with allure.step("Click search button"):
    advanced_search_page.click_search()
  
  with allure.step("Check search results"):
    vacancy_page.check_results_visible()
    vacancy_page.check_salary(CHECK_SALARY_90K)

@allure.story("Advanced Search - Check search by salary -10000 RUB")
def test_negative_salary_filter(advanced_search_page: AdvancedSearchPage, vacancy_page: VacancyPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
  
  with allure.step("Fill salary filter"):
    advanced_search_page.fill_salary(SALARY_LESS_0K)
  
  with allure.step("Click search button"):
    advanced_search_page.click_search()
  
  with allure.step("Check search results"):
    vacancy_page.check_results_visible()
    vacancy_page.check_salary(CHECK_SALARY_10K)

@allure.story("Advanced Search - Check search by salary more than 1000000 RUB")
def test_large_salary_filter(advanced_search_page: AdvancedSearchPage, vacancy_page: VacancyPage):
  with allure.step("Open advanced search page"):
    advanced_search_page.navigate(SEARCH_URL)
  
  with allure.step("Fill salary filter"):
    advanced_search_page.fill_salary(SALARY_1M)
  
  with allure.step("Enable salary only"):
    advanced_search_page.enable_salary_only()
  
  with allure.step("Click search button"):
    advanced_search_page.click_search()
  
  with allure.step("Check search results"):
    vacancy_page.check_results_visible()
    vacancy_page.check_salary(CHECK_SALARY_1M)
