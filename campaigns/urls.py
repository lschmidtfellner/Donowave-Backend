from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet, UserCreate, CustomAuthToken, UserDetail, UserDonations, UserCampaigns, UserList

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/donations/', UserDonations.as_view(), name='user-donations'),
    path('users/<int:pk>/campaigns/', UserCampaigns.as_view(), name='user-campaigns'),
]
