# Generated by Django 4.2.2 on 2023-06-18 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_alter_form_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form',
            new_name='Student',
        ),
    ]
