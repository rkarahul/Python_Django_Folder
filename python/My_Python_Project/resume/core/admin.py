from django.contrib import admin

# Register your models here.
from .models import resume

@admin.register(resume)
class ResumeModeladmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']
