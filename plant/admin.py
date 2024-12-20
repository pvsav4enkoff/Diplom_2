from django.contrib import admin
from plant.models import *
    # Employee, Equipment, Brigade, Repair,Task)

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Segment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(LocationZone)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('zone_location',)

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('full_info', 'description')

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('full_info',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('full_info',)
@admin.register(Task_Object)
class Task_Object(admin.ModelAdmin):
    list_display = ('name',)