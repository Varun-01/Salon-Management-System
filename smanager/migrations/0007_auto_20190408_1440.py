# Generated by Django 2.1.2 on 2019-04-08 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smanager', '0006_auto_20190408_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_date',
        ),
        migrations.AddField(
            model_name='bill',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Conversation Date'),
        ),
    ]
