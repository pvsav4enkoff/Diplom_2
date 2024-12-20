from plant.models import *
task = Equipment.objects.select_related('segment', 'location').all().order_by('id')
for t in task:
    print(t)