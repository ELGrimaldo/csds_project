from django.urls import path
from . import views

urlpatterns = [
    path(r'Discrete_Probability_Distribution/', views.index )
]