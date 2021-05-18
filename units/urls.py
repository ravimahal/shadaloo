from django.urls import path
from . import views

app_name = 'units'

urlpatterns = [
    path('', views.unit_list),
    path('<unit>/review/', views.unit_review, name = 'review'),
    path('<unit>/test/', views.unit_test, name = 'test'),

]
