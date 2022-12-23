from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def feature(request):
    return render(request, 'pages/feature.html')


def team(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/team.html', data)


def testimonial(request):
    return render(request, 'pages/testimonial.html')



def contact(request):
    return render(request, 'pages/contact.html')
