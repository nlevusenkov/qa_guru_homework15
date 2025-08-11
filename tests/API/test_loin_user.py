import allure
from allure_commons.types import Severity, AttachmentType
from dotenv import load_dotenv
from selene import browser, have
from allure_commons._allure import step

load_dotenv()

@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Отправка API запроса на авторизацию")
@allure.story("Отправка API запроса на авторизацию")
@allure.link("https://demowebshop.tricentis.com/login", name="API авторизации")
def test_login_user(base_url, login_user):
    browser.open(base_url)
    login, response = login_user
    with step("Проверяем статус кода"):
        assert response.status_code == 302
        allure.attach(f'Response status code: {response.status_code}', 'Status Code',
                  attachment_type=AttachmentType.TEXT)
    with step("Проверяем что пользователь авторизован"):
        browser.element('[href="/logout"]').should(have.text("Log out"))
        browser.element('.account').should(have.text(login))

