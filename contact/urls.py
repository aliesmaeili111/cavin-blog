from django.urls import path
from .views import contact

app_name = "contact"

urlpatterns = [
    path('pages/', contact,name= "contact"),
]
