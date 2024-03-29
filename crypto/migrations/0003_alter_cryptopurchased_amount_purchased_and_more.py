# Generated by Django 5.0.2 on 2024-02-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_cryptopurchased_amount_invested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopurchased',
            name='amount_purchased',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='cryptopurchased',
            name='quantity_purchased',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='cryptosold',
            name='amount_sold',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='cryptosold',
            name='quantity_sold',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
