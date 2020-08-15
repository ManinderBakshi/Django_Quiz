from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Category, Sets

# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def quiz_cat(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'quiz/quiz_home.html', context)

def get_sets(request, cat_id):
    
    sets = Sets.objects.filter(set_category=cat_id)
    
    print('sss',sets)
    context={
        'sets':sets
    }

    return render(request, 'quiz/sets.html', context)

def quiz(request, set_id):
    set_info = Sets.objects.get(set_id=set_id)

    context = {
        'set_info':set_info
    }

    return render(request, 'quiz/quiz.html', context)