from django.shortcuts import render
from .models import Rubrik

def test(request):
    return render(request, "testapp/test.html", {'rubriks': Rubrik.objects.all()})

def get_rubrik(request):
    pass
