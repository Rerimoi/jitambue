from django.conf import settings
from django.db import models
from django.utils import timezone


# defines each category in SRH i.e GBV,Abortion, Hygiene
class Category(models.Model):
    image=models.ImageField()
    name= models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

