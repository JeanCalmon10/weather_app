from django.urls import path
from . import views

app_name = 'weatherapp'

urlpatterns = [
    path('', views.index, name='index'),
    # path('delete/<int:weather_id>', views.delete_weather, name='delete_weather'),
]
