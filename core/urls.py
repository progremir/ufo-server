from django.urls import path

from core.views import FlightOptimizerView

urlpatterns = [
    path('optimize', FlightOptimizerView.as_view())
]
