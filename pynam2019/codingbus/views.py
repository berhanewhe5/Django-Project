from django.shortcuts import render

from django.shortcuts import render

from .models import Lesson
# Create your views here.

def index(request):
    lessons = Lesson.objects.all()
    return render(
        request,
        'codingbus/index.html',
        {
            "lessons": lessons,
        }
    )

def lesson(request, title):
    lesson = Lesson.objects.get(
        title=title
    )
    return render(request, 'codingbus/post.html',{
        "lesson": lesson,
    })

from django.http import JsonResponse

def api_post(request, id):
    post = Lesson.objects.filter(id=id)
    return JsonResponse([{'title': post.title} for post in posts], safe=False)