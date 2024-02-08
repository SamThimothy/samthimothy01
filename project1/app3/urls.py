from django.urls import path
from . import views


urlpatterns=[
    path('contact/', views.contact_view),
    path('data/', views.data_view),
]