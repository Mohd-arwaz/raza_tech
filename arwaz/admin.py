from django.contrib import admin
from .models import student
# Register your models here.

class StudentAdminCustomise( admin.ModelAdmin ):
    list_display=["Name", "Address"]
    list_display_links=['Name']
    list_editable =['Address']
    list_filter=['Name']
    
    
   
admin.site.register(student, StudentAdminCustomise)