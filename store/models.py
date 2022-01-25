from datetime import timezone
from unicodedata import name
from django.conf import Settings, settings
from django.db import models
from django.http import request
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

    owner = models.ForeignKey(User, related_name='product_owner', on_delete=models.CASCADE)
    is_rented = models.BooleanField(default=False)
    name = models.CharField(max_length=255, db_index=True)
    cost = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to = 'products', null = True, blank = True)
    date_posted = models.DateTimeField(auto_now=timezone.now)
    description = models.TextField(null=True, blank=True)
    tenure_end = models.DateTimeField(auto_now=timezone.now, null=True, blank=True)
    want_to_rent = models.BooleanField(null=True, blank=True)
    want_to_sell = models.BooleanField(null=True, blank=True)
    rent_per_month = models.IntegerField(null=True, blank=True)
    

    def __str__(self) -> str:
        return str(self.name)