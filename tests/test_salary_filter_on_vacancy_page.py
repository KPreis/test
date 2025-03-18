import allure
import pytest
from playwright.sync_api import Page
from pages.vacancy_page import VacancyPage


VACANCY_URL = "https://hh.ru/search/vacancy"
SALARY_LESS_0K = "-10000"
SALARY_1M = "1000000"
CHECK_SALARY_1M_RUB = "от 1 000 000 ₽"
CHECK_SALARY_1M_EUR = "от 1 000 000 €"
CHECK_SALARY_1M_USD = "от 1 000 000 $"



@pytest.fixture
def vacancy_page(page: Page):
  return VacancyPage(page)

@allure.feature("Vacancy Page")
@allure.story("Vacancy Page - Salary Filter")
def test_basic_elements(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)
  
  with allure.step("Check basic elements"):
    assert vacancy_page.profession_input.is_visible()
    assert vacancy_page.search_button.is_visible()

@allure.story("Vacancy Page - Check search by salary only")
def test_salary_filter(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)
  
  with allure.step("Enable salary only"):
    vacancy_page.enable_salary_only()
  
  with allure.step("Check enable salary only"):
    vacancy_page.check_on_enable_salary_only()

@allure.story("Vacancy Page - Check search by salary more than 1000000 RUB")
def test_custom_salary_filter_rubles(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)
  
  with allure.step("Input to custom salary"):
    vacancy_page.fill_custom_salary(SALARY_1M)
  
  with allure.step("Check salary filter"):
    vacancy_page.check_salary(CHECK_SALARY_1M_RUB)

@allure.story("Vacancy Page - Check search by salary more than 1000000 EUR")
def test_salary_custom_filter_euro(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)

  with allure.step("Switch currency to EUR"):
    vacancy_page.switch_currency("EUR")
    
  with allure.step("Input to custom salary"):
    vacancy_page.fill_custom_salary(SALARY_1M)
  
  with allure.step("Check salary filter"):
    vacancy_page.check_salary(CHECK_SALARY_1M_EUR)

@allure.story("Vacancy Page - Check search by salary more than 1000000 USD")
def test_salary_custom_filter_usd(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)

  with allure.step("Switch currency to USD"):
    vacancy_page.switch_currency("USD")
    
  with allure.step("Input to custom salary"):
    vacancy_page.fill_custom_salary(SALARY_1M)
  
  with allure.step("Check salary filter"):
    vacancy_page.check_salary(CHECK_SALARY_1M_USD)

@allure.story("Vacancy Page - Check search by salary -10000 RUB")
def test_salary_filter_negative(vacancy_page: VacancyPage):
  with allure.step("Open advanced search page"):
    vacancy_page.navigate(VACANCY_URL)
  
  with allure.step("Try to fill salary filter with -10000"):
    vacancy_page.fill_custom_salary(SALARY_LESS_0K) #input doesn't support minus value
    vacancy_page.click_search()
  
  with allure.step("Check search results"):
    vacancy_page.check_salary("Не имеет значения")

@allure.story("Vacancy Page - Check search by salary with 0")
def test_salary_custom_filter_input_0(vacancy_page: VacancyPage):
  with allure.step("Open vacancy page"):
    vacancy_page.navigate(VACANCY_URL)
    
  with allure.step("Input to custom salary"):
    vacancy_page.fill_custom_salary("0")
  
  with allure.step("Check salary filter"):
    vacancy_page.check_salary("Не имеет значения")