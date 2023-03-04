
from django.urls import path
from.views import home, cont
urlpatterns =[
    path('', home),
    path('cont', cont)
]