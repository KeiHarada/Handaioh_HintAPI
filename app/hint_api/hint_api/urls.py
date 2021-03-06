"""hint_api URL Configuration

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
from django.contrib import admin
from django.conf.urls import include, url
#from ..api_test.urls import router as hint_test_router
#from ..api_neo4j.urls import
from api_test.urls import router as hint_test_router
from api_neo4j.urls import router as hint_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_test/', include(hint_test_router.urls)),
    url(r'^api/', include(hint_router.urls)),
]
