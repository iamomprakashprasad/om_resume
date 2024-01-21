from rest_framework import serializers
from .models import PermanentAddress, Current_Address, BasicInformation, FamilyDetails
from .models import AttendedSchools, EmployedCompanies, Projects, Skills

class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = (
            "id",
            "first_name",
            "last_name",
            "mobile_no"
        )
