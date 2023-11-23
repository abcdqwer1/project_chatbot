from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('messages', views.MessageViewSet)
router.register('Conversation', views.ConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]