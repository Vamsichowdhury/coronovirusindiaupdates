
from django.urls import path
from .views import home, aboutMe



urlpatterns = [
    path('home/', home, name="home"),
    path('aboutme/', aboutMe, name='aboutme'),
]