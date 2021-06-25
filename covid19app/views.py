from django.shortcuts import render
import requests
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = True
    covid = None
    globaldata = None
    countrydata = None
    while(data):
        try:
            covid = requests.get('https://api.covid19api.com/summary')
            json = covid.json()
            globaldata = json['Global']
            countrydata = json["Countries"]
            data = False
        except:
            data = True
    paginator = Paginator(countrydata,100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'covid19app/home.html',{"covid":globaldata, "countrydata": countrydata, "forms" : page_obj })
