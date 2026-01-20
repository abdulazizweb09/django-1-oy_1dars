"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Kutubxona.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', home, name='home'),
    path('details/<int:id>/', details, name='muallif_details'),
    # path('tirik-mualliflar/', tirik_mualliflar, name='tirik_mualliflar'),
    # path('top-mualliflar/', top_mualliflar, name='top_mualliflar'),
    # path('katta-mualliflar/', katta_mualliflar, name='katta_mualliflar'),

    path('kitoblar/', kitoblar, name='kitoblar'),
    path('kitob/<int:id>/', kitob, name='kitob_details'),
    path('record/',record),
    path('talaba/',talaba),
]
