# Generated by Django 4.2.2 on 2023-06-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_rename_contact_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(default=' ', max_length=50),
        ),
    ]
