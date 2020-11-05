"""students_information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from students import views

urlpatterns = [
    path('', views.fetch_univesity_list, name='fetch_univesity_list'),
    path('login/', views.login, name='login'),
    path('university/', views.fetch_univesity_list, name='fetch_univesity_list'),
    path('college/', views.fetch_college_list, name='fetch_college_list'),
    path('student/', views.fetch_student_list, name='fetch_student_list'),
    path('create/', views.create_university_form, name='create_university_form'),
    path('create/university/', views.create_university, name='create_university'),
    path('error/<str:error_message>/', views.error, name='error'),
    path('success/<str:success_message>/', views.success, name='success'),
    path('admin/', admin.site.urls),

]
