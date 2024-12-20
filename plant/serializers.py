# from rest_framework import serializers
# from .models import Equipment, Repair, Task
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('repair', 'task_object','employee', 'start_date', 'end_date','status','description')
#
# class RepairSerializer(serializers.ModelSerializer):
#     repair_tasks = TaskSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Repair
#         fields = '__all__'
#
# class EquipmentSerializer(serializers.ModelSerializer):
#     repairs = RepairSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Equipment
#         fields = '__all__'