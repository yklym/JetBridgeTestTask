# Generated by Django 3.0.7 on 2020-06-07 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0004_auto_20200607_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viraluser',
            old_name='images',
            new_name='image',
        ),
    ]
