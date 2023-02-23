from rest_framework import routers 
from . serializers import  *
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include




router= routers.DefaultRouter()
router.register(r'User',UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)