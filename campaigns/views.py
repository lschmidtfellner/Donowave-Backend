from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No permission for registration view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def donations(self, request, pk=None):
        user = self.get_object()
        donations = Donation.objects.filter(user=user)
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def campaigns(self, request, pk=None):
        user = self.get_object()
        campaigns = Campaign.objects.filter(user=user)
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated,]
        else:
            self.permission_classes = [AllowAny,]
        return super(CampaignViewSet, self).get_permissions()

    @action(detail=True, methods=['get'])
    def donations(self, request, pk=None):
        campaign = self.get_object()
        donations = Donation.objects.filter(campaign=campaign)
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated,]
        else:
            self.permission_classes = [AllowAny,]
        return super(DonationViewSet, self).get_permissions()

    def perform_create(self, serializer):
        donation = serializer.save()
        campaign = donation.campaign
        campaign.raised_amount += donation.amount
        campaign.save()
