# Generated by Django 3.1.1 on 2020-09-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0002_auto_20200926_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementmodel',
            name='product_Image',
        ),
    ]