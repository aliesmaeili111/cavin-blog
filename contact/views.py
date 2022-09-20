from django.shortcuts import render

from contact.models import Contact
from .forms import ContactForm

def contact(request):
    response_from = ContactForm()
    if request.method == "POST":
        response_from = ContactForm(request.POST)
        if response_from.is_valid():
            response_from.save()
    else:
        response_from = ContactForm()
        
    context={
        'form':response_from
    }
    return render(request,"blog/contact.html",context)
