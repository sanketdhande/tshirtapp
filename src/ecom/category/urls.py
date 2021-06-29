from django.urls import path, include
from rest_framework.authtoken import views
from .views import CategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
