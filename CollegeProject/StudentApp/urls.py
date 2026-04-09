from django.urls import path
from . import views

app_name = 'StudentApp'
urlspattern=[
    path('', views.student_list, name='student_list')
]