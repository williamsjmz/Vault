# Generated by Django 4.0.6 on 2022-07-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0007_alter_address_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Address 2'),
        ),
        migrations.AlterField(
            model_name='paymentcard',
            name='type',
            field=models.CharField(blank=True, choices=[('Credit card', 'Credit card'), ('Debit card', 'Debit card'), ('Charge card', 'Charge card'), ('Pre-paid card', 'Pre-paid card'), ('Business travel card', 'Business travel card'), ('Purchasing card', 'Purchasing card')], default='Credit card', max_length=30, null=True, verbose_name='Type'),
        ),
    ]