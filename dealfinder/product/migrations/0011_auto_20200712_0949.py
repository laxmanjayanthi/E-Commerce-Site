# Generated by Django 2.2.10 on 2020-07-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
