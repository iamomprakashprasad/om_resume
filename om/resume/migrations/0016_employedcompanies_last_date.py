# Generated by Django 5.0.1 on 2024-01-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_remove_employedcompanies_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employedcompanies',
            name='last_date',
            field=models.DateField(null=True),
        ),
    ]
