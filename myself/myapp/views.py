from django.shortcuts import render
from .models import contact
# Create your views here.

def index(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save data to the database
        contact.objects.create(name=name, email=email, message=message)
    return render(request, "index.html", {})
    