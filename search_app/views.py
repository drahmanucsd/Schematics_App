from django.shortcuts import render
from . models import Data

# Create your views here.
def index(request):
    data = Data.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'search_app/index.html', context)