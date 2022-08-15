from django.urls import path, include
from survey import views

urlpatterns = [
    path('', views.home, name='survey_home'),
    path('survey1/', views.survey1, name='survey1'),
    path('form1/', views.form1, name='form1'),
    path('result1/', views.result1, name='result1'),
]