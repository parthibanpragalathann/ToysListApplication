
from django.urls import path,include


#Project of TOYS URLs ...

urlpatterns = [
    path('api/', include('toys_app.urls'))  #Following the path of api site URLs
]