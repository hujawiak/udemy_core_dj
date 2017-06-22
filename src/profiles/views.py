from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from contact.forms import ContactForm
import datetime

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

@login_required
def done(request):
    return render(request, 'done.html')

def about(request):
    success_message = False
    if request.user.is_authenticated() and request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.name = "Dupa"
            new_contact.save()
            success_message = "Form saved"
    else:
        form = ContactForm()
    context = {'image_link': "http://blog.memes.com/wp-content/uploads/2015/09/dickbutt2.png", 'form': form,
               'success_message': success_message}
    return render(request, 'about.html', context)

@login_required
def user_profile(request):
    user = request.user
    context = {'user': user}
    
    return render(request, 'profile.html', context)

def filters(request):
    some_text = "hello, how \nare you on Mondays?"
    number = 12098
    now_date = datetime.datetime.today()
    future_date_time = datetime.datetime.now() + datetime.timedelta(days=9999, hours=23, minutes=59)
    past_date_time = datetime.datetime.now() - datetime.timedelta(days=999, hours=23, minutes=59)
    html_code = "<h1>Dupa html</h1>"
    fpath = "/home/anna/Downloads/prawo.zip"
    
    context = {'some_text': some_text, 'number': number, 'now_date': now_date, 'future_date_time': future_date_time,
               'past_date_time': past_date_time, 'html_code': html_code, 'fpath': fpath}
    
    return render(request, 'filters.html', context)