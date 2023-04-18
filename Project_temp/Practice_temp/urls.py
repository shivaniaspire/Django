from django.urls import path
from Practice_temp import views

urlpatterns = [
    # path("", views.index, name='index')
    path("Practice_temp/", views.index, name='Practice_temp/index')
    
]