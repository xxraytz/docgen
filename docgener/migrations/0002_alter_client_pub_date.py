# Generated by Django 4.0.4 on 2022-05-29 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docgener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]