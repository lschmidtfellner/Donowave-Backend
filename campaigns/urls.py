from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet, UserCreate

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserCreate.as_view(), name='user-register'),
    path('api-auth/', include('rest_framework.urls')),
]