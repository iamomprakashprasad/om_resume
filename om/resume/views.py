from django.shortcuts import render
from rest_framework import generics
from .models import PermanentAddress, Current_Address, BasicInformation, FamilyDetails
from .models import AttendedSchools, EmployedCompanies, Projects, Skills
from .serializers import PermanentAddressSerializer, Current_AddressSerializer, BasicInformationSerializer, FamilyDetailsSerializer
from .serializers import AttendedSchoolsSerializer, EmployedCompaniesSerializer, ProjectsSerializer, SkillsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


#Create your views here.

class BasicInformationList(generics.ListAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializer

class PermanentAddressList(generics.ListAPIView):
    queryset = PermanentAddress.objects.all()
    serializer_class = PermanentAddressSerializer

class Current_AddressList(generics.ListAPIView):
    queryset = Current_Address.objects.all()
    serializer_class = Current_AddressSerializer

class FamilyDetailsList(generics.ListAPIView):
    queryset = FamilyDetails.objects.all()
    serializer_class = FamilyDetailsSerializer

class AttendedSchoolsList(generics.ListAPIView):
    queryset = AttendedSchools.objects.all()
    serializer_class = AttendedSchoolsSerializer

class EmployedCompaniesList(generics.ListAPIView):
    queryset = EmployedCompanies.objects.all()
    serializer_class = EmployedCompaniesSerializer

class ProjectsList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class SkillsList(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

@api_view(["GET"])
def all_apis(request, format=None):
    return Response(
        {
            reverse("information", request=request, format=format),
            # "user-information/<int:pk>", reverse("user-information", request=request, format=format),
            reverse("permanent-address", request=request, format=format),
            # "user-permanent-address", reverse("user-permanent-address", request=request, format=format),
            reverse("current-address", request=request, format=format),
            # "user-current-address", reverse("user-current-address", request=request, format=format),
            reverse("family-details", request=request, format=format),
            # "user-family-details", reverse("user-family-details", request=request, format=format),
            reverse("attended-schools", request=request, format=format),
            # "user-attended-schools", reverse("user-attended-schools", request=request, format=format),
            reverse("employed-companies", request=request, format=format),
            # "user-employed-companies", reverse("user-employed-companies", request=request, format=format),
            reverse("projects", request=request, format=format),
            # "user-projects", reverse("user-projects", request=request, format=format),
            reverse("skils", request=request, format=format),
            # "user-skils", reverse("user-skils", request=request, format=format),
            
        }
    )