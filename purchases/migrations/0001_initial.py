# Generated by Django 4.2.1 on 2023-06-28 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('provider', models.CharField(blank=True, max_length=220, null=True)),
                ('stripe_checkout_session_id', models.CharField(blank=True, max_length=220, null=True)),
                ('stripe_price', models.IntegerField(default=0)),
                ('kakaopay_checkout_tid', models.CharField(blank=True, max_length=20, null=True)),
                ('kakaopay_price', models.IntegerField(default=0)),
                ('products', models.ManyToManyField(to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
