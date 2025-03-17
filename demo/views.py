from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import os
from django.http import FileResponse, HttpResponse



def home(request):
    return render(request, 'home.html')

def art_archive(request):
    return render(request, 'art_archive.html')

def firstpick(request):
    return render(request, 'firstpick.html')

def ivrpov(request):
    return render(request, 'ivrpov.html')


def comfortably_numb(request):
    return render(request, 'comfortably_numb.html')

def bemyangel(request):
    return render(request, 'bemyangel.html')

def brown_dreams(request):
    return render(request, 'brown_dreams.html')

def impressionism(request):
    return render(request, 'impressionism.html')

def realism(request):
    return render(request, 'realism.html')

def SIEVM(request):
    return render(request, 'SIEVM.html')

def me(request):
    return render(request, 'me?.html')

def irony(request):
    return render(request, 'irony.html')

def about_me(request):
    return render(request, 'about_me.html')

def download(request):
    file_path = os.path.join(settings.BASE_DIR, 'static','css', 'pdf', 'port.pdf')
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='port.pdf')
    else:
        return HttpResponse("File not found.", status=404)


def contact(request):
    form = ContactForm()  # Always initialize the form here

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']

            send_mail(
                f'New Contact Form Submission from {name}',
                f'Name: {name}\nPhone: {phone}\nEmail: {email}',
                settings.DEFAULT_FROM_EMAIL,
                ['sarishalekhi@gmail.com'],
            )

            return render(request, 'thank_you.html')
    
    return render(request, 'contact.html', {'form': form})

