from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    path('form', views.myform, name="myform"),
    path('formprocess', views.process, name="process"),
]