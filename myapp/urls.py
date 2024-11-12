from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.home, name=('my_home')),
    path('about/', views.about, name=('my_about')),
    path('service/', views.service, name=('my_service')),
    path('contact/', views.contact, name=('my_contact')),
    path('booking/', views.booking, name=('my_booking')),
]


