# Generated by Django 5.1.3 on 2024-12-12 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0010_alter_repair_end_date_alter_repair_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Объект ремонта',
                'verbose_name_plural': 'Объекты ремонта',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='segment',
        ),
        migrations.AddField(
            model_name='task',
            name='task_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_object_tasks', to='plant.task_object'),
        ),
    ]
