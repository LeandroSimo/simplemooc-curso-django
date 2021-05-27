from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = [
           'name', 'slug', 'start_date', 'create_at'
        ]
    search_fields = ['name', 'slug']
    

admin.site.register(Course, CourseAdmin)
