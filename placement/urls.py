"""placement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from movie.views import myView
from movie.views import homepage
from movie.views import results
from django.conf.urls import include, url

admin.autodiscover()



urlpatterns = [
    path('admin/', admin.site.urls),
     path('m/', myView),
   url(r'', include('index.urls')),
    url(r'^search/', include('index.urls')),

]
