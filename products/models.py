from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import CharField, DecimalField

class Menu(models.Model):
  name = models.CharField(max_length=20)

  class Meta:
    db_table = 'menu'

class Category(models.Model):
  name = models.CharField(max_length=20)
  menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

  class Meta:
    db_table = 'categories'

class Product(models.Model):
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  korean_name = models.CharField(max_length=45)
  english_name = models.CharField(max_length=45)
  description = models.TextField()
  nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

  class Meta:
    db_table = 'products'

class Image(models.Model):
  image_url = models.CharField(max_length=2000)
  product = models.ForeignKey('Product', on_delete=models.CASCADE)

  class Meta:
    db_table = 'images'

class Nutrition(models.Model):
  one_serving_kcal = DecimalField(max_digits=6, decimal_places=2)
  sodium_mg = DecimalField(max_digits=6, decimal_places=2)
  saturated_fat_g = DecimalField(max_digits=6, decimal_places=2)
  sugars_g = DecimalField(max_digits=6, decimal_places=2)
  protein_g = DecimalField(max_digits=6, decimal_places=2)
  caffeine_mg = DecimalField(max_digits=6, decimal_places=2)
  size_ml = CharField(max_length=45)
  size_fluid_ounce = CharField(max_length=45)

  class Meta:
    db_table = 'nutritions'

class Allergy(models.Model):
  name = CharField(max_length=45)

  class Meta:
    db_table = 'allergy'

class Allergy_products(models.Model):
  allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
  product = models.ForeignKey('Product', on_delete=models.CASCADE)

  class Meta:
    db_table = 'allergy_products'

