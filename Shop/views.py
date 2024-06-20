from django.shortcuts import render
from .models import Products
from .forms import ApplicationForm


def home(request):
    product = Products.objects.all()[:9]
    return render(request, 'index.html', {
        'product': product,
    })


def contact(request):
    form = ApplicationForm()
    return render(request, 'contact.html', {
        'form': form
    })

