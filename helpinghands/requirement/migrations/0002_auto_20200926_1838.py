# Generated by Django 3.1.1 on 2020-09-26 13:08

from django.db import migrations, models
import requirement.validators


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementmodel',
            name='product_Image',
            field=models.FileField(upload_to='documents/%Y/%m/%d', validators=[requirement.validators.validate_file_extension]),
        ),
    ]
