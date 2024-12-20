from plant.views import *
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # path('', view_plant),
    path('', login_view, name='login'),
    # admin 123
    path('admin/', admin.site.urls),

    path('plant/', view_plant,name="plant"),

    path('plant/employee/edit/<pk>/', edit_employee, name='edit_employee'),
    path('plant/repair', view_plant_repair,name='repairs_list'),
    path('plant/task', view_plant_task,name='task_list'),
    path('plant/equipment', view_plant_equipment),
    path('plant/employee', view_plant_employee, name='employee_main'),
    path('plant/employee/sign_up', sign_up_by_plant),
    path('plant/equipment/sign_equipment', registration_equipment),
    path('plant/equipment/sign_repair', registration_repair),
    path('plant/employee/sign_task', registration_task),
    path('repair/complete_repair/<pk>/', complete_repair, name='complete_repair'),
    path('task/complete_task/<pk>/', complete_task, name='complete_task'),
    path('plant/task', sort_view, name='sort_view'),

    path('export_to_excel_task/', export_to_excel_task, name='export_to_excel_task'),


]
