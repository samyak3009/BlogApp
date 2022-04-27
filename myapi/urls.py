import imp
from django.db import router
from django.urls import path,include
from myapi import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns=[
    path("hello-view", views.HelloApiView().as_view()),
    path('', include(router.urls))
]