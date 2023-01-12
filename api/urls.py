from django.urls import path
from . import views

urlpatterns = [
    path('employee/<int:employee_id>/photo', views.add_employee_photo),
    path('recognize', views.recognize_employee),
    path('list', views.getData),
    path('employee', views.add_employee)
]
