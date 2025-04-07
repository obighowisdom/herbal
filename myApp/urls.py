from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'myAppurl'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('herbal/', views.herbal, name = 'herbal'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('testimony/', views.testimony, name = 'testimony'),
    path('work/', views.work, name = 'work'),


   

]