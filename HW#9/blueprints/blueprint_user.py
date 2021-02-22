from datetime import datetime
from flask import Blueprint, request
from blueprints.exceptions import NoSuchUser


user_bp = Blueprint('user_bp', __name__, url_prefix='/user_bp')

USERS_DATABASE = {}
CART_DATABASE = {}
user_counter = 1
cart_counter = 1


@user_bp.errorhandler(NoSuchUser)
def no_such_cart_handler(e):
    return {"error": f"no such cart with id {e.cart_id}"}, 404


@user_bp.route('/users', methods=["POST"])
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


@user_bp.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@user_bp.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    user_update = request.json
    try:
        USERS_DATABASE[user_id]['name'] = user_update['name']
        USERS_DATABASE[user_id]['email'] = user_update['email']
    except KeyError:
        raise NoSuchUser(user_id)
    return {"status": "success"}, 201


@user_bp.route('/users/<int:user_id>', methods="DELETE")
def del_user(user_id):
    try:
        del USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    return {"status": "success"}, 200


