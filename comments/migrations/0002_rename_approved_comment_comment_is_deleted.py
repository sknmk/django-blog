# Generated by Django 3.2.5 on 2021-08-08 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='is_deleted',
        ),
    ]
