from flask import Flask
from blueprints.blueprint_cart import cart_bp
from blueprints.blueprint_user import user_bp

amazon_killer = Flask(__name__)
amazon_killer.register_blueprint(user_bp)
amazon_killer.register_blueprint(cart_bp)


if __name__ == "__main__":
    amazon_killer.run(debug=True)
