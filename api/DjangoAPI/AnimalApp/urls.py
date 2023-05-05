from django.urls import re_path
from AnimalApp import views


urlpatterns=[
    re_path(r'^perritos',views.AnimalApi),
    re_path(r'^perritos/([0-9]+)$',views.AnimalApi),

    re_path(r'^accesorios',views.AccesorioApi),
    re_path(r'^accesorios/([0-9]+)$',views.AccesorioApi)

]