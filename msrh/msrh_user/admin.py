from django.contrib import admin

# Register your models here.
from models import HOD, HR, SUPERVISOR,EMPLOYEE, Training, DEPARTMENT

class hod_admin(admin.ModelAdmin):
    list_display = ('Eid', 'name', 'department', 'position')

class hr_admin(admin.ModelAdmin):
    list_display = ('Eid', 'name', 'department', 'position')

class supervisor_admin(admin.ModelAdmin):
    list_display = ('Eid', 'name', 'department', 'position')

class employee_admin(admin.ModelAdmin):
    list_display = ('Eid', 'name', 'department')

class train(admin.ModelAdmin):
    list_display = ('name', 'department', 'venue', 'date', 'time','topic', 'head_of_program')

admin.site.register(HOD, hod_admin)
admin.site.register(HR, hr_admin)
admin.site.register(SUPERVISOR, supervisor_admin)
admin.site.register(EMPLOYEE, employee_admin)
admin.site.register(Training,train)
admin.site.register(DEPARTMENT)