# Generated by Django 3.1.1 on 2020-09-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(upload_to='products/%Y/%m/%d/'),
        ),
    ]