# Generated by Django 3.2 on 2022-11-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_food_pairing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='pairing',
        ),
        migrations.AddField(
            model_name='food',
            name='pairings',
            field=models.ManyToManyField(related_name='pairings', to='products.Pairing'),
        ),
    ]