# Generated by Django 4.1.7 on 2023-03-05 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='name',
            new_name='brand',
        ),
    ]
