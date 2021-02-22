
from flask import Blueprint, request
from blueprints.exceptions import NoSuchCart

cart_bp = Blueprint('cart_bp', __name__, url_prefix='/cart_bp')

CART_DATABASE = {}
cart_counter = 1


@cart_bp.route('/cart', methods="POST")
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


@cart_bp.route('/cart/<int:cart_id>')
def get_cart_info(cart_id):
    try:
        cart = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@cart_bp.route('/cart/<int:cart_id', methods="PUT")
def update_cart_info(cart_id):
    cart_update = request.json
    try:
        CART_DATABASE[cart_id]['products'] = cart_update['products']
    except KeyError:
        raise NoSuchCart(cart_id)
    return CART_DATABASE[cart_id]['products'], 201


@cart_bp.route('/cart/<int:cart_id', methods="DELETE")
def del_cart(cart_id):
    try:
        del CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    return {"status": "success"}, 200


