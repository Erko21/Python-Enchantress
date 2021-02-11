import pytest
import datetime
from database import DatabaseConnection


@pytest.fixture()
def test_fixture():
    test_fixture = DatabaseConnection()
    yield
    test_fixture.cursor.close()
    test_fixture.conn.close()


class TESTS:
    def test_crud_user(self, test_fixture):
        user_info = {"name": "Ernest", "email": "ekedesh@gmail.com", "registration_time": "2021-02-10 14:00:00"}

        test_fixture.create_user(user_info)

        user_id = test_fixture.read_user_info()

        update_user_info = {"id": user_id, "name": "Erko", "email": "ekedesh1@gmail.com",
                            "registration_time": "2021-02-10 20:01:00"}

        assert test_fixture.read_user_info(user_info) == ("Ernest", "ekedesh@gmail.com",
                                                          datetime.datetime(2021, 2, 10, 14, 00, 00))

        test_fixture.update_user(update_user_info)
        assert test_fixture.read_user_info(user_id) == (user_id, "Erko", "ekeedesh1@gmail.com",
                                                        datetime.datetime(2021, 2, 10, 20, 1, 00))

        test_fixture.delete_user(user_id)
        assert test_fixture.read_user_info(user_id) is None

    def test_cart_crud(self, text_fixture):
        user_info = {"name": "master", "email": "mymaster@gmail.com", "registration_time": "2021-02-10 14:11:00"}
        test_fixture.create_cart(user_info)
        user_id = text_fixture.last_created_card()

        new_cart = {"creating_time": "2021-02-10 14:11:00", "user_id": user_id,
                    "cart_details": [{"price": 2000, "product": "computer"}]}

        text_fixture.create_cart(new_cart)
        cart_id = text_fixture.last_created_card()

        assert text_fixture.read_cart(cart_id) == [(datetime.datetime(2021, 2, 10, 14, 11, 00), 200, "computer")]

        text_fixture.delete_cart(cart_id)
        assert text_fixture.read_cart(cart_id) == []
