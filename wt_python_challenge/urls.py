"""wt_python_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.url_patterns import routers
from conditions.views import ConditionViewSet

router = routers.DefaultRouter()
router.register(r'conditions', ConditionViewSet)

urlpatterns = ('',
    url(r'^', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', views.ConditionViewSet.as_view()),
    url(r'^api/$', views.TreatmentViewSet.as_view()),
    url(r'^conditions/', include('conditions.urls'))
)

urlpattern = routers
