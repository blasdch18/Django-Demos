from django.urls import path
from . import views

urlpatterns = [
    #Path core
    path('',views.services,name="services"),



]