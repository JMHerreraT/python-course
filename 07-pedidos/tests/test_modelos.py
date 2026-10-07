import pytest
from pydantic import ValidationError

from pedidos.modelos import Order, Product

ORDER_JSON = """
{
  "customer": "Ana",
  "discount": 0.1,
  "products": [
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 50, "quantity": 2}
  ]
}
"""


def test_order_from_json_calculates_total():
    order = Order.model_validate_json(ORDER_JSON)

    assert order.total() == 1168.2


def test_empty_products_raises_error():
    with pytest.raises(ValidationError):
        Order.model_validate({"customer": "Ana", "products": []})


def test_negative_price_raises_error():
    with pytest.raises(ValidationError, match=r"products\.0\.price"):
        Order.model_validate({
            "customer": "Ana",
            "products": [{"name": "Laptop", "price": -100, "quantity": 1}],
        })


def test_discount_above_max_raises_error():
    with pytest.raises(ValidationError, match="discount"):
        Order.model_validate({
            "customer": "Ana",
            "discount": 0.5,
            "products": [{"name": "Laptop", "price": 1000, "quantity": 1}],
        })


def test_price_as_string_is_converted():
    product = Product.model_validate({"name": "Mouse", "price": "50", "quantity": 1})

    assert product.price == 50.0
    assert isinstance(product.price, float)