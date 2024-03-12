"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):

        # TODO напишите проверки на метод check_quantity

        assert product.check_quantity(1000) == True

        assert product.check_quantity(999) == True

        assert product.check_quantity(1001) == False

        try:
            product.check_quantity(-1)

            product.check_quantity(0)

        except TypeError:
            pass






    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900
        product.buy(900)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        try:
            product.buy(1001)
        except ValueError:
            pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 5)
        assert cart.products[product] == 6

    def test_dell_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.remove_product(product, 1)
        assert cart.products[product] == 4
        cart.remove_product(product)
        assert product not in cart.products.keys()
        cart.add_product(product, 5)
        cart.remove_product(product, 6)
        assert product not in cart.products.keys()

    def test_clear_card(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert product not in cart.products.keys()

    def test_total_price(self, product, cart):
        cart.add_product(product, 5)
        assert cart.get_total_price() == product.price * 5
        cart.add_product(product)
        assert cart.get_total_price() == (product.price * 5) + product.price

    def test_buy(self, product, cart):
        with pytest.raises(ValueError):
            cart.buy()
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990
        assert not cart.products
        cart.add_product(product, 1000)
        with pytest.raises(ValueError):
            cart.buy()
        cart.remove_product(product, 1000)
        assert cart.products[product] == 0
        cart.add_product(product, 3)
        cart.clear()
        assert not cart.products