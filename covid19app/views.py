from django.shortcuts import render
import requests

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
    return render(request, 'covid19app/home.html',{"covid":globaldata, "countrydata": countrydata})
