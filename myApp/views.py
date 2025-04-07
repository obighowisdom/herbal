from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages


from .models import testimonie
from .models import product
from .models import contacts



# Create your views here.

def home(request):

    pro = product.objects.all()


    return render(request, 'home.html', {'pro':pro})

def about(request):

    return render(request, 'about.html')

def herbal(request):

    return render(request, 'herbal.html')

def testimonial(request):

    fam = testimonie.objects.all()

    return render(request, 'testimonial.html', {'fam':fam})

def testimony(request):



    return render(request, 'testimony.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']


        user_request = contacts(name=name, email=email, subject=subject, body=body)
        user_request.save()
        messages.success(request, f'Message Submitted... You will be contacted shortly through the email you provided')
        return redirect("index:contact")  

    return render(request, 'contact.html')

def work(request):

    return render(request, 'work.html')



