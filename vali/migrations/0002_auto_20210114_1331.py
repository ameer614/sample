# Generated by Django 3.1.5 on 2021-01-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vali', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]