from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet, UserCreate, UserViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('api-auth/', include('rest_framework.urls')),
]
