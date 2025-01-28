from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=["id","name","address","age","mobile_number"]
    list_display_links=["name"]

admin.site.register(Student,StudentAdmin)
