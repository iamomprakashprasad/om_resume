# Generated by Django 5.0.1 on 2024-01-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_employedcompanies_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinformation',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
