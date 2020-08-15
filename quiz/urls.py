
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/categories/', views.quiz_cat, name='categories'),
    path('quiz/categories/<int:cat_id>/', views.get_sets, name='sets'),
    path('quiz/categories/sets/<int:set_id>/', views.quiz, name='quiz')
]
