# Generated by Django 3.1.5 on 2021-01-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vali', '0005_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default='base.jpeg', upload_to='product_photos'),
        ),
    ]