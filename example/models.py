from django.db import models
from django.contrib import admin
from django_numerators.models import NumeratorMixin


# Create your models here.

class Product(NumeratorMixin):
    class Meta:
        verbose_name = "Product"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['inner_id', 'name', 'created_at']
