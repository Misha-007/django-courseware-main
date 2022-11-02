from django.contrib import admin
from classroom.models import Course, Category,Grade,Schedule,Attendance

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attendance)