from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Map
import pandas as pd
import geopandas as gpd
from django.conf import settings
i

# Create your views here.
def home(request):
    return render(request,'home.html')
