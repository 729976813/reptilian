"""reptilian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from reptilian.Reptilian import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^company/', include('reptilian.Reptilian.get_information.urls')),
    url(r'^test2$', TemplateView.as_view(template_name='findcompany.html'), name='company'),
    url(r'^area/', include('reptilian.Reptilian.get_information.urls')),
    url(r'^industry/', include('reptilian.Reptilian.get_information.urls')),
    url(r'^analysis/', TemplateView.as_view(template_name='companyanalysis.html'), name='analysis'),
    url(r'^find/', include('reptilian.Reptilian.get_information.urls'), name='find'),
]
