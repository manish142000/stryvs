from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'products')
    phone = models.IntegerField()
    address = models.TextField() 

    def __str__(self) -> str:
        return f'{ self.user.username } Profile'


class Transactions(models.Model):
    user = models.ForeignKey(User, related_name="related_user", on_delete = models.CASCADE)
    product = models.OneToOneField(Product, related_name="product_transacted", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{ self.product.name } Transaction'


class Appointments(models.Model):
    appointment_accepter = models.ForeignKey(User, related_name="seller_appointment", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name="for_appointment", on_delete=models.CASCADE)
    appointment_maker = models.ForeignKey(User, related_name="customer_appointment", on_delete=models.CASCADE) 
    appointment_date = models.DateField()
    appointment_time = models.TimeField(auto_now=False)
    appointment_subject = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{ self.product.name }'