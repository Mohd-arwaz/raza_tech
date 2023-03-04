
from django.urls import path
from .views import home, team, services, contact
urlpatterns = [
    path('', home),
    path('team', team ),
    path('services', services ),
    path('contact', contact )
    
]