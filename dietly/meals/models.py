import datetime

from django.db import models
from django.utils import timezone

class Meals(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20, blank=True, null=True)
    mealname = models.CharField(db_column='mealName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    menumealname = models.CharField(db_column='menuMealName', max_length=600, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    dietaryfiber = models.FloatField(db_column='dietaryFiber', blank=True, null=True)  # Field name made lowercase.
    sugar = models.FloatField(blank=True, null=True)
    salt = models.FloatField(blank=True, null=True)
    saturatedfattyacids = models.FloatField(db_column='saturatedFattyAcids', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.CharField(max_length=6000, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meals'
    

    

