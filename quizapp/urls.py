from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TestViewSet, UserViewSet, QuestionsViewSet, OptionsViewSet, AnswersViewSet

router=DefaultRouter()
router.register('test',TestViewSet)
router.register('user',UserViewSet)
router.register('questions',QuestionsViewSet)
router.register('Options',OptionsViewSet)
router.register('answers',AnswersViewSet)
urlpatterns=[path('',include(router.urls))]


