from django.contrib import admin

from .models import PermanentAddress, Current_Address, BasicInformation, FamilyDetails
from .models import AttendedSchools, EmployedCompanies, Projects, Skills

# Register your models here.

admin.site.register(PermanentAddress)
admin.site.register(Current_Address)
admin.site.register(BasicInformation)
admin.site.register(FamilyDetails)
admin.site.register(AttendedSchools)
admin.site.register(EmployedCompanies)
admin.site.register(Projects)
admin.site.register(Skills)

