# Generated by Django 4.2.6 on 2024-01-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='images'),
        ),
    ]