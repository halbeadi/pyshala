from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Question, Choice, QuizResult

def quiz_list(request):
    quizzes = Quiz.objects.filter(is_published=True)
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, is_published=True)
    questions = quiz.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        score = 0
        total = questions.count()
        results = []

        for question in questions:
            selected_id = request.POST.get(f'question_{question.id}')
            correct_choice = question.choices.filter(is_correct=True).first()
            selected_choice = None

            if selected_id:
                try:
                    selected_choice = Choice.objects.get(id=selected_id)
                    if selected_choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

            results.append({
                'question': question,
                'selected': selected_choice,
                'correct': correct_choice,
                'is_correct': selected_choice and selected_choice.is_correct,
            })

        percentage = round((score / total) * 100) if total > 0 else 0
        passed = percentage >= 60

        # Save result
        QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total=total,
            percentage=percentage,
            passed=passed
        )

        return render(request, 'quiz/quiz_result.html', {
            'quiz': quiz,
            'results': results,
            'score': score,
            'total': total,
            'percentage': percentage,
            'passed': passed,
        })

    return render(request, 'quiz/quiz_detail.html', {
        'quiz': quiz,
        'questions': questions,
    })