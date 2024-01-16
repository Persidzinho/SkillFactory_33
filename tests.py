import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.mark.auth
def test_tabs_on_page(web_browser):
    page = AuthPage(wev_browser)

    tabs_elements = [x.text for x in page.tabs]
    for x in page.tabs:
        assert x.is_enabled()
        assert x.is_displayed()
    assert page.tab_phone.is_clickable() and page.tab_email.is_clickable()
    assert 'Телефон' in tabs_elements and 'Почта' in tabs_elements
    print('\n Tabs on page')


def test_valid_name_lastname(web_browser):
    page = PageRegistration(web_browser)
    WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    page.btn_enter.click()
    WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    page.link_enter.click()
    web_browser.implicitly_wait(10)
    page.name.send_keys('Имя')
    page.last_name.send_keys('Фамилия')
    time.sleep(5)
    page.select_town.send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + 'Москва')
    time.sleep(5)
    page.email_and_mobile.send_keys('nik.chvanov.05bk.ru@gmail.com')
    assert PageRegistration.is_loaded()


def test_authorization(web_browser):
    page = AuthPage(web_browser)
    WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    page.btn_enter.click()
    WebDriverWait(web_browser, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    page.link_enter.click()
    assert page.email_and_mobile.is_presented()

def test_login_page_allert(web_browser):
    page = AuthPage(web_browser)
    page.delete_all_cookies()
    page.username_input.send_keys('SomeBugInHere')
    page.password_input.send_keys('123456789')
    page.submit_btn.click()
    unvalid_err = page.error_msg.get_text()
    assert 'Неверный логин или пароль' in unvalid_err


def test_registration(web_browser):
    main_page = MainPage(browser)
    main_page.page_loading()
    assert main_page.is_loaded()
    main_page.search_registr()


def test_btn_help(web_browser):
    page = AuthPage(web_browser)
    page.btn_help.click()
    page.link_help()
    assert btn_help.enter()
