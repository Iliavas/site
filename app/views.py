from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from random import choice
from collections import namedtuple
from .mixins import rendering


def index(request):
    ctx = {}
    a = list(ClassMates.objects.all())
    teachers = list(Teachers.objects.all())
    for i in range(6):
        b = choice(a)
        ctx.update({str(str(i) + 'random_people'): b})
        a.remove(b)
    for i in range(3):
        b = choice(teachers)
        ctx.update({str(str(i) + 'random_teachers'): b})
        teachers.remove(b)
    return render(request, 'app/base.html', context=ctx)


def RenderClass(request):
    return rendering(request, ClassMates, 'app/classmates.html', 'classmates')


def RenderTeachers(request):
    return rendering(request, Teachers, 'app/teachers.html', 'teachers')
