# Generated by Django 3.2 on 2022-10-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_guid',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
