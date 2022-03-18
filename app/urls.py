from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('results/', views.products),
    path('customer/', views.customer),
    path('tracker/', views.covidTrackerForm),
    path('QA_team_records/', views.QA_records),
    path('Data_team_records/', views.Data_team_records),
    path('Development_records/', views.Development_records),

]