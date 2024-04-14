# Generated by Django 3.2.24 on 2024-04-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_alter_membership_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='cost',
        ),
        migrations.AddField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='membership',
            name='stripe_price_id',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='membership',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='membership',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]