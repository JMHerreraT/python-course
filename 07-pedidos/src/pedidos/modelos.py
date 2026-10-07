from pydantic import BaseModel, Field

from .settings import settings


class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(default=1, ge=1)


class Order(BaseModel):
    customer: str = Field(min_length=1)
    products: list[Product] = Field(min_length=1)
    discount: float = Field(default=0, ge=0, le=settings.max_discount)

    def total(self) -> float:
        subtotal = sum(product.price * product.quantity for product in self.products)
        discounted = subtotal * (1 - self.discount)
        return round(discounted * (1 + settings.igv), 2)