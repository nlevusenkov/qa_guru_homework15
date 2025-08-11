import time
from allure_commons._allure import step
from selene import browser, have, be

def test_product_basket(login_user):
    product_name = "$25 Virtual Gift Card"  # переменная с названием товара

    with step("Открываем страницу корзины"):
        browser.element('[href="/cart"]').click()

    with step("Проверка добавления товара в корзину через UI"):
        browser.all('.product-name').element_by(have.text(product_name)).should(be.visible)
