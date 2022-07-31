from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    unisport_id = models.CharField(max_length=6)
    name = models.TextField()  # Or VARCHAR?
    relative_url = models.CharField(max_length=255)
    image = models.URLField()
    delivery = models.CharField(max_length=255)
    online = models.BooleanField(default=False)
    is_customizable = models.BooleanField(default=False)
    is_exclusive = models.BooleanField(default=False)
    url = models.URLField()

    @property
    def stock(self):
        return Stock.objects.filter(product_id=self.pk)

    @property
    def sizes_in_stock(self):
        return [stock_item.size for stock_item in self.stock if stock_item.stock_quantity > 0]

    @property
    def price(self):
        return Price.objects.filter(product_id=self.pk)

    # Set default order to max_price from Price model
    class Meta:
        ordering = ['price__max_price']

    def __str__(self):
        return f'{self.pk}/{self.unisport_id} - {self.name}'


class Stock(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # Name from API?
    stock_quantity = models.IntegerField()  # Additional
    is_marketplace = models.BooleanField()
    name_short = models.CharField(max_length=30)
    # order_by = models.IntegerField() # From API
    # pk = models.IntegerField() # From API

    # Create unique constraint on product + size
    class Meta:
        db_table = 'stock'
        constraints = [models.UniqueConstraint(
            fields=['product_id', 'size'], name='unique product size')]

    def __str__(self):
        return f'{self.product_id} - {self.size} - {self.stock_quantity}'


class Currency(models.Model):
    currency_code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.currency_code}'


class Price(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=8, decimal_places=2)
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.IntegerField()
    recommended_retail_price = models.DecimalField(
        max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.product_id} - {self.currency}: {self.max_price}, Discount: {self.discount_percentage}%'
