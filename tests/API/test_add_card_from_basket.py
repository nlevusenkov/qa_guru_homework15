
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import Severity, AttachmentType


@allure.tag("API")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Отправка API запроса на добавления заказа в корзину")
@allure.story("Отправка API запроса на добавления заказа в корзину")
@allure.link("https://demowebshop.tricentis.com/addproducttocart/details/", name="API добавления в корзину")
def test_add_card_from_basket(base_url, login_user):
    with step("Добавляем товары в корзину"):
        product_id = 72
        quantity = 1
        cookies, _ = login_user
        response = requests.post(url=base_url + f"/addproducttocart/details/{product_id}/{quantity}", cookies={'NOPCOMMERCE.AUTH': cookies})
    with step("Проверяем код ответа"):
        assert response.status_code == 200
        allure.attach(f'Response status code: {response.status_code}', 'Status Code',
                  attachment_type=AttachmentType.TEXT)