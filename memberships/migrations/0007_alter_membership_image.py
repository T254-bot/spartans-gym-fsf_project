# Generated by Django 3.2.24 on 2024-05-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0006_membership_stripe_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='image',
            field=models.ImageField(upload_to='static/media/site_images/image.jpg'),
        ),
    ]
