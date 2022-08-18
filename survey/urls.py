from django.urls import path, include
from survey import views

urlpatterns = [
    path('', views.home, name='survey_home'),
    path('survey1/', views.survey1, name='survey1'),
    path('survey3/', views.survey3, name='survey3'),
    path('form1/', views.form1, name='form1'),
    path('form3/', views.form3, name='form3'),
    path('result1/', views.result1, name='result1'),
    path('result3/', views.result3, name='result3'),
]