# Generated by Django 3.1.1 on 2020-10-25 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.seat'),
        ),
    ]
