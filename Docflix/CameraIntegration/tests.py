from django.test import TestCase

# Create your tests here.
from django.urls import path
from . import views
urlpatterns = [
    path('camera/', views.livefe),
    path('product1/',views.page1),
    path('product2/',views.page2),
    path('symptom/',views.symptom),
    path('disease/',views.predict),
    path('',views.home,name="home"),
]
