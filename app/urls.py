from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classmates', views.RenderClass, name='classmates'),
    path('teachers', views.RenderTeachers, name='teachers')
]