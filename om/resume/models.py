from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PermanentAddress(models.Model):
    house_no = models.TextField(max_length=20)
    street = models.TextField(max_length=20)
    village = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)

class Current_Address(models.Model):
    house_no = models.TextField(max_length=20)
    street = models.TextField(max_length=20)
    village = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    at_location_from = models.DateField()
    till_at_location = models.DateField(null=True, blank=True)

class BasicInformation(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_no = PhoneNumberField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    email_id = models.EmailField()
    open_to_work = models.BooleanField()
    married = models.BooleanField()
    alternate_mobile_no = PhoneNumberField()
    dob = models.DateField()
    whatsapp = PhoneNumberField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    permanent_address = models.ForeignKey(PermanentAddress, on_delete=models.CASCADE)
    about = models.TextField(default="")
    


class FamilyDetails(models.Model):
    relation_choices = (
        ("brother", "Brother"),
        ("sister", "Sister"),
        ("father", "Father"),
        ("mother", "Mother"),
    )
    relation = models.CharField(choices=relation_choices, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = PhoneNumberField()
    email_id = models.EmailField()
    married = models.BooleanField()
    occupation = models.TextField()


class AttendedSchools(models.Model):
    marks_type = (
        ('cgpa', 'CGPA'),
        ('percentage', 'Percentage')
    )
    school_name = models.TextField()
    first_year = models.DateField()
    final_year = models.DateField()
    marks_type = models.CharField(choices=marks_type, max_length=20)
    marks_optained = models.FloatField()
    location = models.TextField()

class EmployedCompanies(models.Model):
    company_name = models.TextField()
    company_url = models.URLField(default="")
    joined_at = models.DateField()
    current_company = models.BooleanField()
    last_date = models.DateField(null=True)
    description = models.TextField()

class Projects(models.Model):
    project_name = models.CharField(max_length=20)
    url = models.URLField(null=1)
    description = models.TextField()
    associated_with = models.ForeignKey(EmployedCompanies, on_delete=models.CASCADE)

class Skills(models.Model):
    choices = tuple((level, str(level)) for level in range(11))
    skill_name = models.CharField(max_length=20)
    skill_level = models.IntegerField(default=8, choices=choices)
    associated_with_projects = models.ManyToManyField(Projects)
    associated_with_companies = models.ManyToManyField(EmployedCompanies)



