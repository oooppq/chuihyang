"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from accounts import views as accounts_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('perfumes/<int:id>', views.perfumes, name='perfumes'),
    path('new_review/<int:id>', views.new_review, name='new_review'),


    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),

    path('reviews/', views.reviews, name='reviews'),
    path('ranking/', views.ranking, name='ranking'),
    path('search/', views.search, name='search'),
    path('searched/', views.searched, name='searched'),

    # path('survey/', views.survey, name='survey'),
    path('survey/', include('survey.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
