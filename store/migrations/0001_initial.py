# Generated by Django 4.0.1 on 2022-01-25 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rented', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('tenure_end', models.DateTimeField(auto_now=True, null=True)),
                ('want_to_rent', models.BooleanField(blank=True, null=True)),
                ('want_to_sell', models.BooleanField(blank=True, null=True)),
                ('rent_per_month', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
