import pytest
from Amazon_killer import amazon_killer as app
from freezegun import freeze_time


@pytest.fixture
def get_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(get_app):
    response = get_app.post(
        '/users',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com",
         })
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": '2021-02-08T14:16:41.892824',
    }
    user_id = response.json['user_id']
    response = get_app.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json == {
        "name": "Illia",
        "email": "illia.sukonnik@gmail.com",
        "user_id": user_id,
        "registration_timestamp": '2021-02-08T14:16:41'
    }


def test_no_such_user(get_app):
    response = get_app.get('users/2')

    assert response.status_code == 404
    assert response.json == {"error": "no such user with id 2"}


def test_update_user(get_app):
    response = get_app.put(
        '/users/1',
        json={
                "name": "Ernest",
                "email": "ekedesh@gmail.com"
        }
    )
    assert response.status_code == 200

    response = get_app.put(
        '/users/2',
        json={
            "name": "Ernest",
            "email": "ekedesh@gmail.com"
        }
    )
    assert response.status_code == 404
    assert response.json == {"error": "no such user with id 3"}


def test_delete_user(get_app):
    response = get_app.delete('/users/1')
    assert response.status_code == 200

    response = get_app.delete('/users/2')
    assert response.status_code == 404
    assert response.json == {"error": "no such user with id 2"}


@freeze_time('2021-02-08 14:16:41')
def test_create_cart(get_app):
    response = get_app.post(
        '/cart',
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'Book: how to stop be boring',
                    "price": 500,
                },
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        }
    )
    assert response.status_code == 201
    assert response.json == {
        "cart_id": 1,
        "creation_time": '2021-02-08T14:16:41'
    }

    cart_id = response.json['cart_id']
    response = get_app.get(f'/cart/{cart_id}')

    assert response.status_code == 200
    assert response.json == {
        "cart_id": cart_id,
        "user_id": 1,
        "creation_time": '2021-02-08T14:16:41',
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }


def test_no_such_cart(get_app):
    response = get_app.get('/cart/2')
    assert response.status_code == 404
    assert response.json == {"error": "no such cart with id 2"}


def test_update_cart(get_app):
    response = get_app.put(
        '/cart/1',
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        }
    )
    assert response.status_code == 200

    response = get_app.put(
        '/cart/2',
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        }
    )
    assert response.status_code == 404
    assert response.json == {"error": "no such cart with id 2"}


def test_delete_cart(get_app):
    response = get_app.delete('/cart/1')
    assert response.status_code == 200
    response = get_app.delete('/cart/2')
    assert response.status_code == 404
    assert response.json == {"error": "no such cart with id 2"}
