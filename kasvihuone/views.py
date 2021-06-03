from django.shortcuts import render
from .models import *

# Create your views here.
def greenhouse_home(request):
    # greenhouses = Greenhouse.objects.all()
    # humidity = Humidity.objects.all()
    # soil_moisture = Soilmoisture.objects.all()
    # temperature = Temperature.objects.all()
    # for gh in Greenhouse.objects.all():
    #     print(gh)
    #     # print(testi)
    #     pass
    # greenhouses = {
    #     # 
    # }

    # for gh in Greenhouse.objects.all():
    #     planters = {}
    #     for planter in gh.planter_set.all():
    #         mvalues = {}
    #         for moisture in planter.soilmoisture_set.all()[:5]:
    #             mvalues[moisture.date] = moisture.value
    #         planters[planter.plants] = mvalues
    #     temperatures = {}
    #     for temperature in gh.temperature_set.all()[:5]:
    #         temperatures[temperature.date] = temperature.value
    #     hum = {}
    #     for humidity in gh.humidity_set.all()[:5]:
    #         hum[humidity.date] = humidity.value
    #     # greenhouses[gh.greenhouse] = [planters, temperatures, hum]
    #     greenhouses[gh.greenhouse] = {
    #         'planters' : planters,
    #         'temperatures' : temperatures,
    #         'humidity' : hum
    #     }
    # print(greenhouses)
    content = {
        'title' : 'Greenhouses',
        'Greenhouses' : Greenhouse.objects.all(),
    }
 
    return render(request, 'kasvihuone/greenhouse.html', content)