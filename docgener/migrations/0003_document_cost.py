# Generated by Django 4.0.4 on 2022-05-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docgener', '0002_alter_client_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]