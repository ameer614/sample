# Generated by Django 3.1.5 on 2021-01-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vali', '0002_auto_20210114_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
