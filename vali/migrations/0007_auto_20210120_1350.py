# Generated by Django 3.1.5 on 2021-01-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vali', '0006_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default='base.jpg', upload_to='product_photos'),
        ),
    ]
