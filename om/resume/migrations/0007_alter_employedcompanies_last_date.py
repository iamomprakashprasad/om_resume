# Generated by Django 5.0.1 on 2024-01-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_employedcompanies_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedcompanies',
            name='last_date',
            field=models.DateField(null=True),
        ),
    ]