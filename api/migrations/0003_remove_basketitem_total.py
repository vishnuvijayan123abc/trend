# Generated by Django 4.2.6 on 2024-01-11 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='total',
        ),
    ]