# Generated by Django 3.2.7 on 2021-10-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20211016_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
