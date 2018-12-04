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
from django.views.generic import TemplateView
from reptilian.Reptilian.get_information import views



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='findcompany.html'), name='find'),
    url(r'^find/', views.CompanyView.as_view(), name='company'),
    url(r'^create/', views.CreateCompanyView.as_view(), name='create'),
    url(r'^total/', TemplateView.as_view(template_name='areatotal.html'), name='areatotal'),
    url(r'^total2/', TemplateView.as_view(template_name='industrytotal.html'), name='industrytotal'),
    url(r'^data/', views.TotalAreaView.as_view(), name='data'),
    url(r'^data2/', views.OneIndustryView.as_view(), name='data2'),
    url(r'^data3/', views.OneAreaView.as_view(), name='data3'),
    url(r'^map/', TemplateView.as_view(template_name='areamap.html'), name='areamap'),
    url(r'^total2/', TemplateView.as_view(template_name='industrytotal.html'), name='industrytotal'),
    url(r'^computer/', TemplateView.as_view(template_name='computer.html'), name='computer'),
    url(r'^signal/', TemplateView.as_view(template_name='signal.html'), name='signal'),
    url(r'^henan/', TemplateView.as_view(template_name='henan.html'), name='sichuan'),
    url(r'^sichuan/', TemplateView.as_view(template_name='sichuan.html'), name='henan'),
    url(r'^data4/', views.AnalysisView.as_view(), name='data4'),
    url(r'^data5/', views.AreaMapView.as_view(), name='data5'),
    url(r'^data6/', views.TotalIndustryView.as_view(), name='data6'),
]
