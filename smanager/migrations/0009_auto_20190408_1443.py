# Generated by Django 2.1.2 on 2019-04-08 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smanager', '0008_auto_20190408_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Bill date'),
        ),
    ]