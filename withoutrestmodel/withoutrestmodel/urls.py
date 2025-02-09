"""
URL configuration for withoutrestmodel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',views.EmployeeDetailCBV.as_view()),
    path('api/',views.EmployeeCRUDCBV.as_view()),
    path('api/<int:id>/',views.EmployeeDetailCBV2.as_view()),
    path('apise/<int:id>/',views.EmployeeDetailCBV3.as_view()),
    path('apiall/',views.EmployeeDetailCBV4.as_view()),
    path('apione/<int:id>/',views.EmployeeDetailCBV5.as_view()),
]
