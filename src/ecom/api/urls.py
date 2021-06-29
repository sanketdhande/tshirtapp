from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('home/',home),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
