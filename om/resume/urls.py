from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("info/", views.BasicInformationList.as_view(), name="information"),
    path("info/<int:pk>/", views.BasicInformationList.as_view(), name="user-information"),
    path('permanent-address/', views.PermanentAddressList.as_view(), name="permanent-address"),
    path('permanent-address/<int:pk>/', views.PermanentAddressList.as_view(), name="user-permanent-address"),
    path('current-address/', views.Current_AddressList.as_view(), name="current-address"),
    path('current-address/<int:pk>/', views.Current_AddressList.as_view(), name="user-current-address"),
    path('family-details/', views.FamilyDetailsList.as_view(), name="family-details"),
    path('family-details/<int:pk>/', views.FamilyDetailsList.as_view(), name="user-family-details"),
    path('attended-schools/', views.AttendedSchoolsList.as_view(), name="attended-schools"),
    path('attended-schools/<int:pk>/', views.AttendedSchoolsList.as_view(), name="user-attended-schools"),
    path('employed-companies/', views.EmployedCompaniesList.as_view(), name="employed-companies"),
    path('employed-companies/<int:pk>/', views.EmployedCompaniesList.as_view(), name="user-employed-companies"),
    path('projects/', views.ProjectsList.as_view(), name="projects"),
    path('projects/<int:pk>/', views.ProjectsList.as_view(), name="user-projects"),
    path('skils/', views.SkillsList.as_view(), name="skils"),
    path('skils/<int:pk>/', views.SkillsList.as_view(), name="user-skils"),
    path("", views.all_apis),
]

urlpatterns = format_suffix_patterns(urlpatterns)