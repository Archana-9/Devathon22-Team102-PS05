from django.contrib import admin
from .models.student import Student
from .models.issue import Issue
from .models.type import Type
from .models.category import Category
from .models.stat import Stat
from .models.plumber import Plumber

 
 
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','branch','hostel_name','room_no','phone_no','email','password']

class AdminType(admin.ModelAdmin):
    list_display = ['typename']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminIssue(admin.ModelAdmin):
    list_display = ['description','category','student','type','date','status']

class AdminPlumber(admin.ModelAdmin):
    list_display = ['description','room','date','stat']

class AdminStat(admin.ModelAdmin):
    list_display = ['statname']

# Register your models here.

admin.site.register(Student,AdminStudent)
admin.site.register(Issue,AdminIssue)
admin.site.register(Category,AdminCategory)
admin.site.register(Type,AdminType)
admin.site.register(Plumber,AdminPlumber)
admin.site.register(Stat,AdminStat)
