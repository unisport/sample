from django.db import models
from django.db.models import F
"""
    Models for backend:

    Add test data by running the following commands:
        python manage.py provision
        python manage.py add_unisport_data
    
    4 models:
        Product (Generic product data)
        Stock (Stock data about each product in stock. Foreign Key - references Product model)
        Currency (Decided to do a seperate currency model in case of multiple currencies)
        Prices (Seperate Price model to allow each product to have prices in multiple currencies. Foreign Key - references Product model)

        This implementation lacks the fields: labels and attributes from unisport API.
        Could be added using models.JSONField()
"""


class Product(models.Model):
    unisport_id = models.CharField(max_length=6, unique=True, db_index=True)
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
        return [stock_item.name_short for stock_item in self.stock if stock_item.stock_quantity > 0]

    @property
    def prices(self):
        return Price.objects.filter(product_id=self.pk)

    @property
    def price_dkk(self):
        return Price.objects.get(product_id=self.pk).max_price

    @property
    def min_price_dkk(self):
        return Price.objects.get(product_id=self.pk, currency_code='SEK').min_price

    @property
    def current_price(self):
        return Price.objects.get(product_id=self.pk).get_current_price

    @property
    def get_discount_percentage(self):
        return Price.objects.get(product_id=self.pk).discount_percentage

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

    @property
    def get_current_price(self):
        return self.max_price - self.max_price * self.discount_percentage / 100

    def __str__(self):
        return f'{self.product_id} - {self.currency}: {self.max_price}, Discount: {self.discount_percentage}%'


## Price.objects.annotate(current_price=F('max_price') - F('max_price') * F('discount_percentage') / 100)

# Price objects ordered by calculated current_price - applying discounts:

# low to high
# order = Price.objects.annotate(current_price=F('max_price') - F('max_price') * F('discount_percentage') / 100).order_by('current_price').order_by('current_price')

# high to low
# order = Price.objects.annotate(current_price=F('max_price') - F('max_price') * F('discount_percentage') / 100).order_by('current_price').order_by('current_price')


### Product.objects.all().annotate(discount_price=F('price__max_price') - F('price__max_price') * F('price__discount_percentage') / 100).order_by('discount_price')
