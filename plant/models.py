from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()

    class Meta:
        ordering = ['start_date']  # сортировка по start_date

# Бригада
class Brigade(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='brigade_leader')
    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
    def __str__(self):
        return self.name
# Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    boss = models.BooleanField(default=False)
    activ = models.BooleanField(default=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_employees')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class Position(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
class LocationZone(models.Model):
    zone_location = models.CharField(max_length=25)
    class Meta:
        verbose_name = "Локализация"
        verbose_name_plural = "Локализации"
    def __str__(self):
        return self.zone_location
class Segment(models.Model):
    name = models.CharField(max_length=125)
    class Meta:
        verbose_name = "Сегмент"
        verbose_name_plural = "Сегменты"
    def __str__(self):
        return self.name
class Task_Object(models.Model):
    name = models.CharField(max_length=125)
    class Meta:
        verbose_name = "Объект ремонта"
        verbose_name_plural = "Объекты ремонта"
    def __str__(self):
        return self.name
# Оборудование
class Equipment(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='equipment_name')
    description = models.TextField(default=None)
    location = models.ForeignKey(LocationZone, on_delete=models.CASCADE, related_name='equipment_location')
    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"
    @property
    def full_info(self):
        return f"{self.segment} - {self.location}"
# Ремонт
class Repair(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='repairs')
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='brigade_repairs')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=25)


    class Meta:
        verbose_name = "Площадка ремонта"
        verbose_name_plural = "Площадка ремонта"
    @property
    def full_info(self):
        return f"{self.equipment.segment} - {self.brigade} - {self.status}  начало {self.start_date} окончание {self.end_date}"
    @property
    def select_info(self):
        return f"{self.equipment.location} -{self.equipment.segment} - {self.brigade} - {self.status}  начало {self.start_date}"

    @property
    def complect_info(self):
        return (
                f"""{self.equipment.segment}\n
                {self.brigade}\n
                начало ремонта: {self.start_date}\n"""
                )

    @property
    def dates_info(self):
        if self.end_date:
            return f"Начало: {self.start_date}, Окончание: {self.end_date}"
        else:
            return f"Начало: {self.start_date}, Окончание: не задано"
# Задача
class Task(models.Model):
    task_object = models.ForeignKey(Task_Object, on_delete=models.CASCADE, related_name='task_object_tasks', verbose_name='Объект ремонта')
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name='repair_tasks', verbose_name='Ремонт')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_tasks', verbose_name='Исполнитель')
    employee_status = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(verbose_name='Начало ремонта')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Окончание ремонта')
    status = models.CharField(max_length=25, verbose_name='Статус')


    class Meta:
        verbose_name = "Ремонт объекта"
        verbose_name_plural = "Ремонт объекта"
    @property
    def full_info(self):
        return f"{self.employee.name} - {self.task_object} - {self.status} начало {self.start_date} окончание {self.end_date}"
    # def __str__(self):
    #     return self.name
    @property
    def complete_info(self):
        return f"{self.employee.name} - {self.task_object} - {self.status} начало {self.start_date} "

class plant_post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title