"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest import views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'products', views.FreshProductViewSet, base_name='product')
router.register(r'categories', views.CategoryViewSet, base_name='category')

schema_view = get_swagger_view(title='API Doc')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^doc/', schema_view)
#    url(r'^products/$', views.ProductView.as_view()),
#    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view()),
#    url(r'^categories/$', views.CategoryView.as_view()),
#    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetailView.as_view()),
]
