"""rpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import register, login_view, user_logout
from rpiapp.views import tabulation, SubjectCreateView, SubjectListView, SubjectDetailView, SubjectUpdateView, \
    StudentCreateView, StudentListView, StudentDetailView, StudentUpdateView, tabulations

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tabulation),
    url(r'^register/$', register),
    url(r'^login/$', login_view),
    url(r'^logout/$', user_logout),
    url(r'^subject/create/$', SubjectCreateView.as_view(), name='subject_create_view'),
    url(r'^subject/list/$', SubjectListView.as_view(), name='subject_list_view'),
    url(r'^subject/(?P<slug>[-\w]+)$', SubjectDetailView.as_view(), name='subject_details_view'),
    url(r'^subject/(?P<slug>[-\w]+)/update/$', SubjectUpdateView.as_view(), name='subject_update_view'),

    url(r'^student/create/$', StudentCreateView.as_view(), name='student_create_view'),
    url(r'^student/list/$', StudentListView.as_view(), name='student_list_view'),
    url(r'^student/(?P<slug>[-\w]+)$', StudentDetailView.as_view(), name='student_details_view'),
    url(r'^student/(?P<slug>[-\w]+)/update/$', StudentUpdateView.as_view(), name='student_update_view'),


    url(r'^tabulation$', tabulations, name='tabulation'),
    url(r'^register/$', register),
    url(r'^login/$', login_view),
    url(r'^logout/$', user_logout),



]
