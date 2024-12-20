from plant.models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=255)
    password = forms.CharField(label='Пароль', max_length=255, widget=forms.PasswordInput)


class EmployeeRegistr(forms.Form):
    name = forms.CharField(max_length=50, label= 'ФИО:')
    position = forms.CharField(max_length=50, label= 'Должность:')
    boss = forms.BooleanField(label='Руководитель:', required=False)
    brigade = forms.CharField(max_length=50, label= 'Бригада:')

class BookFilterForm(forms.Form):
    class Meta:
        model = Task
        fields = ('start_date',)
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'position', 'boss', 'brigade', 'activ')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('segment','location','description')


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('equipment', 'brigade', 'start_date')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('repair', 'task_object','employee', 'employee_status', 'start_date')

class CompleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('end_date',)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', _('Дата окончания не может быть меньше даты начала'))

class CompleteRepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('end_date',)