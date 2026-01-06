from django.contrib import admin
from django.urls import include, path
from .views import *

app_name = 'projects'

urlpatterns = [
    path('projects/', projects, name="projects"),
    path('projects/<int:pk>', project_detail, name="project_detail"),

]