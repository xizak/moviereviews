# Generated by Django 4.0 on 2023-06-09 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_review_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='wtachAgain',
            new_name='watchAgain',
        ),
    ]