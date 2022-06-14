"""money_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from money.views import *
from rest_framework import routers
from money.apiViews import *
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter(trailing_slash=True)
router.register("transactions", MoneyViewSet, basename="transactions")
router.register("user", APIUserViewSet, basename="transactions")

# api swagger drf-spectiacular

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # swagger API
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # user auth login
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # main
    path('admin/', admin.site.urls),
    path('add/', AddTransactionView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('signup/', UserSignUpView.as_view()),
    path('view/', ViewTransactionsView.as_view()),
    path('home/', HomeView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('', include('router.urls'))
] + router.urls
