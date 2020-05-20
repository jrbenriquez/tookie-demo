from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from demo.views import SampleObjectViewSet

router = DefaultRouter()

router.register('sample-object', SampleObjectViewSet, 'sample-object')

urlpatterns = [
    path('', include(router.urls))
]