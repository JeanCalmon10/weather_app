from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import City
from .forms import CityForm
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
def index(request):
    cities = City.objects.all()  # Return all the cities in the database.
    

    if request.method == 'POST':  # Only true if form is submitted.
        form = CityForm(request.POST)  # Add actual request data to form for processing.
        form.save()

    form = CityForm()
    weather_data = []
    for city in cities:
        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={os.environ.get('OPENWEATHERMAP_API_KEY')}'
            ).json()

        fahrenheit_temp = city_weather['main']['temp']  # Temperature from the API.
        celsius_temp = (fahrenheit_temp - 32) * 5/9  # Converted temperature to Celsius degrees.

        weather = {
            'city': city,
            'temperature': round(celsius_temp),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)
    
    context = {'weather_data': weather_data, 'form': form}

    
    return render(request, 'weatherapp/index.html', context)