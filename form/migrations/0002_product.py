# Generated by Django 4.0.3 on 2022-03-17 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('product_desc', models.TextField(max_length=200)),
            ],
        ),
    ]
