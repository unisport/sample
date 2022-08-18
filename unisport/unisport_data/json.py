from typing import Dict, List, Optional

import structlog
from django.db import transaction
from pydantic import BaseModel, HttpUrl

import unisport.unisport_data.models as models

logger = structlog.get_logger(__name__)


class Prices(BaseModel):
    max_price: int
    min_price: int
    currency: str
    discount_percentage: int
    recommended_retail_price: int


class Stock(BaseModel):
    price: int
    name: str
    order_by: int
    stock_info: Optional[str]
    is_marketplace: bool
    pk: int
    name_short: str


class Product(BaseModel):
    id: int
    prices: Prices
    name: str
    relative_url: str
    image: HttpUrl
    delivery: str
    online: bool
    labels: List[Dict]
    is_customizable: bool
    is_exclusive: bool
    stock: List[Stock]
    currency: str
    url: HttpUrl
    attributes: Dict


class UnisportProducts(BaseModel):
    products: List[Product]


def create_product_from_json(product: Product) -> models.Product:
    """
    factory method to create a Product model instance from json
    """

    logger.info("Importing product", id=product.id)

    try:
        currency = models.Currency.objects.get(pk=product.currency)
    except models.Currency.DoesNotExist:
        logger.error(
            "Failed to locate currency during product import",
            currency=product.currency,
            product_id=product.id,
        )
        raise

    product_model = models.Product(
        id=product.id,
        currency=currency,
        name=product.name,
        attributes=product.attributes,
        labels=product.labels,
        relative_url=product.relative_url,
        image=str(product.image),
        delivery=product.delivery,
        online=product.online,
        is_customizable=product.is_customizable,
        is_exclusive=product.is_exclusive,
        url=str(product.url),
        max_price=product.prices.max_price,
        min_price=product.prices.min_price,
        discount_percentage=product.prices.discount_percentage,
        recommended_retail_price=product.prices.recommended_retail_price,
    )

    with transaction.atomic():
        for stock in product.stock:
            stock_model = create_stock_from_json(stock)
            stock_model.product = product_model
            stock_model.save()

        product_model.save()

    return product_model


def create_stock_from_json(stock: Stock) -> models.Stock:
    """
    factory method to create a Stock model instance from json
    """
    stock_model = models.Stock(
        id=stock.pk,
        price=stock.price,
        name=stock.name,
        order_by=stock.order_by,
        stock_info=stock.stock_info,
        is_marketplace=stock.is_marketplace,
        name_short=stock.name_short,
    )

    return stock_model
