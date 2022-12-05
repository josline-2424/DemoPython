from django.shortcuts import render
from django.http import HttpResponse
from . models import special_offer

# Create your views here.
def demo(request):
    obj=special_offer.objects.all()
    return render(request, "index.html", {'result': obj})
