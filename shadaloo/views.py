from django.http import HttpResponse
from django.shortcuts import render
from units.models import Word

def homepage(request):
    # return HttpResponse("homepage")
    word_of_the_day = Word.objects.all().order_by('?').first()
    return render(request, "homepage.html", {'word_of_the_day' : word_of_the_day})