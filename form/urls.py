from django.urls import path, include
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from  .views import Userview
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/froms', Userview, basename='forms')

urlpatterns = [
    path('', include(router.urls)),
    path('form/', views.testing, name='form'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]