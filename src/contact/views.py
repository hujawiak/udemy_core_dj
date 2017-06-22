from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    title = "Contact"
    confirm_message = None
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            name = form.cleaned_data['name']
            sbj = 'Message from Dupa.com'
            msg = '%s %s' % (comment, name)
            frm = form.cleaned_data['email']
            to_us = [settings.EMAIL_HOST_USER]
            
            send_mail(sbj, msg, frm, to_us, fail_silently=True)
            title = "Thank you"
            confirm_message = "Thank you for your stupid message. \nStick it up your ass!"
            form = None
            
    context = {'title': title, 'confirm_message': confirm_message, 'form': form}
    
    return render(request, 'contact.html', context)