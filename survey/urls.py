from django.urls import path, include
from survey import views

urlpatterns = [
    path('', views.home, name='survey_home'),
    path('first-survey/', views.first_survey, name='first_survey'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result'),
]