from rest_framework import serializers
from .models import PermanentAddress, Current_Address, BasicInformation, FamilyDetails
from .models import AttendedSchools, EmployedCompanies, Projects, Skills

class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = '__all__'

class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddress
        fields = '__all__'

class Current_AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current_Address
        fields = '__all__'

class FamilyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetails
        fields = '__all__'

class AttendedSchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendedSchools
        fields = '__all__'

class EmployedCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployedCompanies
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
