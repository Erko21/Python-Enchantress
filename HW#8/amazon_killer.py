from flask import Flask, request
from datetime import datetime
from exceptions import NoSuchCart, NoSuchUser

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
CART_DATABASE = {}
user_counter = 1
cart_counter = 1


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {f'"error": "no such user with id {e.user_id}"'}, 404


@amazon_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(e):
    return {"error": f"no such cart with id {e.cart_id}"}, 404


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user
    user_counter += 1
    return response, 201


@amazon_killer.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    user_update = request.json
    try:
        USERS_DATABASE[user_id]['name'] = user_update['name']
        USERS_DATABASE[user_id]['email'] = user_update['email']
    except KeyError:
        raise NoSuchUser(user_id)
    return {"status": "success"}, 201


@amazon_killer.route('/users/<int:user_id>', methods="DELETE")
def del_user(user_id):
    try:
        del USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    return {"status": "success"}, 200


@amazon_killer.route('/cart', methods="POST")
def create_cart():
    global cart_counter
    cart = request.json
    response = {
                    "cart_id": 1,
                    "creation_time": '2021-02-08T14:16:41.892824'
    }
    cart["registration_timestamp"] = response['registration_timestamp']
    cart["cart_id"] = cart_counter
    CART_DATABASE[cart_counter] = cart
    cart_counter += 1
    return response, 201


@amazon_killer.route('/cart/<int:cart_id>')
def get_cart_info(cart_id):
    try:
        cart = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amazon_killer.route('/cart/<int:cart_id', methods="PUT")
def update_cart_info(cart_id):
    cart_update = request.json
    try:
        CART_DATABASE[cart_id]['products'] = cart_update['products']
    except KeyError:
        raise NoSuchCart(cart_id)
    return CART_DATABASE[cart_id]['products'], 201


@amazon_killer.route('/cart/<int:cart_id', methods="DELETE")
def del_cart(cart_id):
    try:
        del CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    return {"status": "success"}, 200


if __name__ == '__main__':
    amazon_killer.run(debug=True)
