# Generated by Django 3.1.5 on 2021-02-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='', max_length=20),
        ),
    ]