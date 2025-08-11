import allure
import pytest
import requests
import os

from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selene import browser
from allure_commons._allure import step

load_dotenv()
@pytest.fixture(scope='session')
def base_url():
    base_url = os.getenv("BASE_URL")
    return base_url
@pytest.fixture(scope='session')
def login_user(base_url):

    login = os.getenv("LOGIN_EMAIL")
    password = os.getenv("PASSWORD")
    with step("Отправляем запрос на авторизацию через API"):
        response = requests.post(
            url=base_url + '/login',
            data={"Email": login, "Password": password, "RememberMe": "false"},
            allow_redirects=False
        )
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    with step("Открываем сайт и подставляем куки"):
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.open(base_url)
        browser.driver.add_cookie({
            'name': 'NOPCOMMERCE.AUTH',
            'value': cookies
        })

    return login, response