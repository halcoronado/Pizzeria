# Generated by Django 3.0.5 on 2022-05-06 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_topping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
    ]
