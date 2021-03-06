from django.urls import path
from . import views

app_name = 'travelhub'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('countries/', views.CountriesIndexView.as_view(), name='countriesindex'),
    path('cities/', views.CitiesIndexView.as_view(), name='citiesindex'),
    path('countries/<slug:slug>', views.CountryDetailView.as_view(), name='countrydetail'),
    path('cities/<slug:slug>', views.CityDetailView.as_view(), name='citydetail'),
]