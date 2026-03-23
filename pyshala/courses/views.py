from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson, Progress

def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lessons = course.lessons.all()
    completed_lessons = []
    if request.user.is_authenticated:
        completed_lessons = Progress.objects.filter(
            user=request.user,
            lesson__course=course,
            completed=True
        ).values_list('lesson_id', flat=True)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'completed_lessons': completed_lessons,
    })

@login_required
def lesson_detail(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug, is_published=True)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course)
    lessons = course.lessons.all()

    # Mark as complete
    progress, created = Progress.objects.get_or_create(
        user=request.user,
        lesson=lesson,
        defaults={'completed': True}
    )
    if not progress.completed:
        progress.completed = True
        progress.save()

    # Next lesson
    next_lesson = course.lessons.filter(order__gt=lesson.order).first()
    prev_lesson = course.lessons.filter(order__lt=lesson.order).last()

    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'lessons': lessons,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson,
    })