"""hrdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from edata.views import *

urlpatterns = [
    url(r'^$','edata.views.index', name='home'),
    url(r'^EmployeeForm/$', 'edata.views.emp_form', name='empform'),
    url(r'^search=(?P<suggestion>\d+)/$', 'edata.views.mysearch', name='mysearch'),
    url(r'^employee_list/$', 'edata.views.employee_list', name='emplist'),
    url(r'^admin/', admin.site.urls)
]
