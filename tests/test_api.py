import pytest  # noqa: F401
import allure
import requests
from config.settings import API_BASE_URL, AUTH_TOKEN

# Заголовки для API-запросов
headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}


@allure.feature("API Тесты")
@allure.story("Самовывоз из магазина")
def test_store_pickup_order():
    # URL для добавления товара в корзину
    add_to_cart_url = f"{API_BASE_URL}/cart/product"
    add_to_cart_payload = {
        "id": 3079434,
        "adData": {
            "item_list_name": "product-page"
        }
    }

    with allure.step("Добавление товара в корзину"):
        add_to_cart_response = requests.post(
            add_to_cart_url, json=add_to_cart_payload, headers=headers
        )
        assert add_to_cart_response.status_code == 200

    # URL для создания заказа
    create_order_url = f"{API_BASE_URL}/orders"
    order_payload = {
        "cityId": 213,
        "shipment": {
            "type": "shop",
            "id": 19,
            "pointId": 117759
        },
        "paymentType": "cash",
        "useAmountBonusPay": 0,
        "user": {
            "type": "individual",
            "name": "Оксана Медведева",
            "phone": "79106347517",
            "email": "oksana090714med@bk.ru",
            "emailNotifications": True,
            "smsNotifications": True,
            "userId": 22224844
        },
        "legalEntity": None,
        "address": {
            "index": None,
            "street": None,
            "house": None,
            "building": None,
            "block": None,
            "apartment": None,
            "fullAddress": "ул. Маршала Бирюзова, д. 17",
            "comment": None
        },
        "shelf": "",
        "listName": "",
        "deliveryDate": "2025-04-15T13:17:34+03:00",
        "bonusPayment": 0,
        "orderType": "rocket"
    }

    with allure.step("Создание заказа на самовывоз из магазина"):
        order_response = requests.post(
            create_order_url, json=order_payload, headers=headers
        )
        assert order_response.status_code == 200

    # Получение ID заказа из ответа
    order_id = order_response.json().get("id")
    assert order_id is not None

    # URL для проверки заказа по ID
    check_order_url = f"{API_BASE_URL}/orders/{order_id}"

    with allure.step("Проверка заказа по ID"):
        check_order_response = requests.get(
            check_order_url, headers=headers
        )
        assert check_order_response.status_code == 200


@allure.feature("API Тесты")
@allure.story("Самовывоз из пункта выдачи")
def test_pickup_point_order():
    # URL для добавления товара в корзину
    add_to_cart_url = f"{API_BASE_URL}/cart/product"
    add_to_cart_payload = {
        "id": 3032550,
        "adData": {
            "item_list_name": "product-page"
        }
    }

    with allure.step("Добавление товара в корзину"):
        add_to_cart_response = requests.post(
            add_to_cart_url, json=add_to_cart_payload, headers=headers
        )
        assert add_to_cart_response.status_code == 200

    # URL для создания заказа
    create_order_url = f"{API_BASE_URL}/orders"
    order_payload = {
        "cityId": 213,
        "shipment": {
            "type": "pickup",
            "id": 34,
            "pointId": 969
        },
        "paymentType": "cash",
        "useAmountBonusPay": 0,
        "user": {
            "type": "individual",
            "name": "Оксана Медведева",
            "phone": "79106347517",
            "email": "oksana090714med@bk.ru",
            "emailNotifications": True,
            "smsNotifications": True,
            "userId": 22224844
        },
        "legalEntity": None,
        "address": {
            "index": None,
            "street": None,
            "house": None,
            "building": None,
            "block": None,
            "apartment": None,
            "fullAddress": "Москва г, Михневский пр-д, 4 стр.1",
            "comment": None
        },
        "shelf": "",
        "listName": "",
        "deliveryDate": "2025-04-05T20:00:00+03:00",
        "bonusPayment": 0,
        "orderType": "order"
    }

    with allure.step("Создание заказа на самовывоз из пункта выдачи"):
        order_response = requests.post(
            create_order_url, json=order_payload, headers=headers
        )
        assert order_response.status_code == 200

    # Получение ID заказа из ответа
    order_id = order_response.json().get("id")
    assert order_id is not None

    # URL для проверки заказа по ID
    check_order_url = f"{API_BASE_URL}/orders/{order_id}"

    with allure.step("Проверка заказа по ID"):
        check_order_response = requests.get(
            check_order_url, headers=headers
        )
        assert check_order_response.status_code == 200


@allure.feature("API Тесты")
@allure.story("Доставка курьером с оплатой при получении")
def test_courier_delivery_order():
    # URL для добавления товара в корзину
    add_to_cart_url = f"{API_BASE_URL}/cart/product"
    add_to_cart_payload = {
        "id": 3025372,
        "adData": {
            "item_list_name": "product-page"
        }
    }

    with allure.step("Добавление товара в корзину"):
        add_to_cart_response = requests.post(
            add_to_cart_url, json=add_to_cart_payload, headers=headers
        )
        assert add_to_cart_response.status_code == 200

    # URL для создания заказа
    create_order_url = f"{API_BASE_URL}/orders"
    order_payload = {
        "cityId": 213,
        "shipment": {
            "type": "courier",
            "id": 34,
            "pointId": 969
        },
        "paymentType": "cash",
        "useAmountBonusPay": 0,
        "user": {
            "type": "individual",
            "name": "Оксана Медведева",
            "phone": "79106347517",
            "email": "oksana090714med@bk.ru",
            "emailNotifications": True,
            "smsNotifications": True,
            "userId": 22224844
        },
        "legalEntity": None,
        "address": {
            "index": None,
            "street": None,
            "house": None,
            "building": None,
            "block": None,
            "apartment": None,
            "fullAddress": "Москва г, Михневский пр-д, 4 стр.1",
            "comment": None
        },
        "shelf": "",
        "listName": "",
        "deliveryDate": "2025-04-05T20:00:00+03:00",
        "bonusPayment": 0,
        "orderType": "order"
    }

    with allure.step("Создание заказа на доставку"
                     " курьером с оплатой при получении"):
        order_response = requests.post(
            create_order_url, json=order_payload, headers=headers
        )
        assert order_response.status_code == 200

    # Получение ID заказа из ответа
    order_id = order_response.json().get("id")
    assert order_id is not None

    # URL для проверки заказа по ID
    check_order_url = f"{API_BASE_URL}/orders/{order_id}"

    with allure.step("Проверка заказа по ID"):
        check_order_response = requests.get(
            check_order_url, headers=headers
        )
        assert check_order_response.status_code == 200


@allure.feature("API Тесты")
@allure.story("Добавление другого товара в корзину")
def test_add_another_product_to_cart():
    # URL для добавления товара в корзину
    add_to_cart_url = f"{API_BASE_URL}/cart/product"
    add_to_cart_payload = {
        "id": 3079435,
        "adData": {
            "item_list_name": "product-page"
        }
    }

    with allure.step("Добавление другого товара в корзину"):
        add_to_cart_response = requests.post(
            add_to_cart_url, json=add_to_cart_payload, headers=headers
        )
        assert add_to_cart_response.status_code == 200


@allure.feature("API Тесты")
@allure.story("Удаление товара из корзины")
def test_remove_product_from_cart():
    # URL для добавления товара в корзину
    add_to_cart_url = f"{API_BASE_URL}/cart/product"
    add_to_cart_payload = {
        "id": 215144143,
        "adData": {
            "item_list_name": "product-page"
        }
    }

    with allure.step("Добавление товара в корзину"):
        add_to_cart_response = requests.post(
            add_to_cart_url, json=add_to_cart_payload, headers=headers
        )
        assert add_to_cart_response.status_code == 200

    # URL для удаления товара из корзины
    remove_from_cart_url = f"{API_BASE_URL}/cart/product/215144143"

    with allure.step("Удаление товара из корзины"):
        remove_from_cart_response = requests.delete(
            remove_from_cart_url, headers=headers
        )
        assert remove_from_cart_response.status_code == 204
