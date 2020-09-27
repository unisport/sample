from django.db import models

# Create your models here.
class Products(models.Model):
  CHOICE_AGE = (
    (1, "Adults"),
    (2, "Kids"),
  )
  CHOICE_GENDER = (
    (1, "Male"),
    (2, "Female")
  )

  class Meta:
    verbose_name="Product"
    verbose_name_plural="Products"
  
  id = models.AutoField(primary_key=True)
  name = models.CharField(
    default="",
    max_length=100
  )
  price = models.FloatField(
    default=""
  )
  age = models.IntegerField(
    default=1,
    choices=CHOICE_AGE
  )
  gender = models.IntegerField(
    default=1,
    choices=CHOICE_GENDER
  )
  
  def __str__(self):
    return f"{self.name} for age {self.age}"