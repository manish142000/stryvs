from django.contrib import admin
# Register your models here.
from .models import Profile, Transactions, Appointments

admin.site.register(Profile)
admin.site.register(Transactions)
admin.site.register(Appointments)