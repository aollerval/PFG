from django.urls import include, path

from rest_framework import routers

from backend.views import UserViewSet, QuestionnaireViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'questionnaire', QuestionnaireViewSet)

urlpatterns = [
    path('', include(router.urls))
]
