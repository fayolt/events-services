# Generated by Django 3.1.1 on 2020-10-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20201025_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tickettype',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tickettype_seats', to='tickets.tickettype'),
        ),
    ]