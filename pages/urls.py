from django.urls import path
from . import views

# the first parameter of path is actually an regex
urlpatterns = [
    path('', views.homePageView, name='home'),
]