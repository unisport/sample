from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


class Currency(models.Model):
    """
    Currency
    """

    id = models.CharField(max_length=3, primary_key=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} - {self.description}"

    class Meta:
        db_table = "currency"


class Stock(models.Model):
    """
    Stock
    """

    id = models.SmallIntegerField(primary_key=True)
    product = models.ForeignKey(
        to="Product", on_delete=models.CASCADE, related_name="stock_items"
    )
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    order_by = models.SmallIntegerField()
    stock_info = models.TextField(default="")
    is_marketplace = models.BooleanField()
    name_short = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.id} - {self.name_short}"

    class Meta:
        db_table = "stock"


class Product(models.Model):
    """
    Product
    """

    id = models.PositiveBigIntegerField(primary_key=True)
    attributes = models.JSONField()
    labels = models.JSONField(default=list, null=False, blank=True)
    name = models.TextField()
    relative_url = models.TextField(max_length=250)
    image = models.URLField()
    delivery = models.TextField(max_length=50)
    online = models.BooleanField()
    is_customizable = models.BooleanField()
    is_exclusive = models.BooleanField()
    url = models.URLField()
    max_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    discount_percentage = models.PositiveSmallIntegerField(default=0)
    recommended_retail_price = models.PositiveIntegerField()

    @property
    def stock(self) -> QuerySet:
        return Stock.objects.filter(product_id=self.id)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    def get_absolute_url(self) -> str:
        return reverse("web:product-detail", args=[self.id])

    class Meta:
        db_table = "product"
        ordering = ["recommended_retail_price"]
