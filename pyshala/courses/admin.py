from django.contrib import admin
from .models import Course, Lesson, Progress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'order', 'created_at']
    list_editable = ['is_published', 'order']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['course']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'completed_at']

