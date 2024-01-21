# Generated by Django 5.0.1 on 2024-01-21 12:25

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendedSchools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.TextField()),
                ('first_year', models.DateField()),
                ('final_year', models.DateField()),
                ('marks_type', models.CharField(choices=[('cgpa', 'CGPA'), ('percentage', 'Percentage')], max_length=20)),
                ('marks_optained', models.FloatField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Current_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.TextField(max_length=20)),
                ('street', models.TextField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('block', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('at_location_from', models.DateField()),
                ('till_at_location', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployedCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField()),
                ('joined_at', models.DateField()),
                ('current_company', models.BooleanField()),
                ('last_date', models.DateField(null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(choices=[('brother', 'Brother'), ('sister', 'Sister'), ('father', 'Father'), ('mother', 'Mother')], max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email_id', models.EmailField(max_length=254)),
                ('married', models.BooleanField()),
                ('occupation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.TextField(max_length=20)),
                ('street', models.TextField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('block', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('github_url', models.URLField()),
                ('linkedin_url', models.URLField()),
                ('email_id', models.EmailField(max_length=254)),
                ('open_to_work', models.BooleanField()),
                ('married', models.BooleanField()),
                ('alternate_mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('dob', models.DateField()),
                ('whatsapp', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('permanent_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.permanentaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('url', models.URLField(null=1)),
                ('description', models.TextField()),
                ('associated_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.employedcompanies')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_level', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=8)),
                ('associated_with_companies', models.ManyToManyField(to='resume.employedcompanies')),
                ('associated_with_projects', models.ManyToManyField(to='resume.projects')),
            ],
        ),
    ]