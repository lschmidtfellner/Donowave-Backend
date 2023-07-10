from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No permission for registration view

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]  # User must be authenticated

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]  # User must be authenticated

    def perform_create(self, serializer):
        donation = serializer.save()
        campaign = donation.campaign
        campaign.raised_amount += donation.amount
        campaign.save()
