"""ZipCode_project URL Configuratio
n
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
# from ajax_select import urls as ajax_select_urls
from zipcode_getter_app import views

urlpatterns = [
	path('', views.home, name='home'),
    path('zipcode_getter', views.zipcode_getter, name = 'zipcode_getter'),
    # path('ajax_select/', admin.site.urls),
    # path('zipcode_getter_app/', include(ajax_select_urls)),
] # + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)