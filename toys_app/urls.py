from .views import *
from django.urls import path
#TOYS application urls ...
urlpatterns = [
    path('toys/', CreateViewToys.as_view(), name="studentsview"),        #all the TOYS details using GET and POST.
    path('toys/<int:pk>/', ModifyViewToys.as_view(), name="addstudsmarks"),  #update particular TOYS using PUT and DELETE
    path('toy/<int:pk>/', ToyView.as_view(), name="particularstudentmark"),   #particular TOYS name using GET
]

