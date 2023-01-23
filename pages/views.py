from django.shortcuts import render, redirect
from .models import Team
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']


        email_subject = 'You have a new message from Othoi website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            subject,
            message_body,
            'Your mail',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')


    return render(request, 'pages/contact.html')
