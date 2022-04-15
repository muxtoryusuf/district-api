from django.urls import path
from . import views

app_name = "district"

urlpatterns = (
    path('api/<str:region>', views.RegionDistrictsAPIView.as_view(), name='api_district'),
)
