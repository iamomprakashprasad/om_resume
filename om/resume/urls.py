from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("info/", views.BasicInformationList.as_view()),
    path("info/<int:pk>/", views.BasicInformationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)