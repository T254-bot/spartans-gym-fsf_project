# Generated by Django 3.2.24 on 2024-05-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0007_alter_membership_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='image',
        ),
    ]
