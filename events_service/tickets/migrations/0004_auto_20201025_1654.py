# Generated by Django 3.1.1 on 2020-10-25 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20201025_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tickettype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickettype_seats', to='tickets.tickettype'),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together=set(),
        ),
    ]
