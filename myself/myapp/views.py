from django.shortcuts import render,redirect
from .models import contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def index(request):
    mob = '+919696160943'
    email_1 = 'kk919844@gmail.com'
    

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
       
       # Save data to the database
        sav = contact.objects.create(name=name, email=email,phone = phone, message=message)
        sav.save()
        

        # send email
        send_mail(
            f"New Contact Form Submission from {name}",
            f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            ['kk919844@gmail.com'],  # Replace with your email
            fail_silently=False,
            )
        messages.success(request, "Your message was submitted successfully! \n We will touch you soon")
       
        return redirect('/')
      
    
           
    return render(request, "index.html", {'phone':mob, 'email_1':email_1})
