from django.shortcuts import render
from .models import Unit, Word
from django.http import HttpResponse

# Create your views here.
def unit_list(request):
    units = Unit.objects.all().order_by("number")
    return render(request, "units/unit_list.html", {'units' : units} )

def unit_review(request, unit):
    #return HttpResponse(unit)
    unit = Unit.objects.get(unit_name = unit)
    words = unit.word_set.all()
    return render(request, "units/review.html", {'words' : words} )

def unit_test(request, unit):
    return HttpResponse(unit)