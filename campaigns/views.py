from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK
from .models import Campaign, Donation
from .permissions import IsAuthenticatedAndIsOwner, LoggedInAndReadOnly
from .serializers import CampaignSerializer, DonationSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No permission for registration view

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndIsOwner,]  

class UserDonations(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [LoggedInAndReadOnly,]

    def get_queryset(self):
        user_id = self.kwargs['pk']  # updated here
        return Donation.objects.filter(user_id=user_id)

class UserCampaigns(generics.ListAPIView):
    serializer_class = CampaignSerializer
    permission_classes = [LoggedInAndReadOnly,]

    def get_queryset(self):
        user_id = self.kwargs['pk']  # updated here
        return Campaign.objects.filter(user_id=user_id)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=HTTP_200_OK)

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [LoggedInAndReadOnly,]

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [LoggedInAndReadOnly,]

    def perform_create(self, serializer):
        donation = serializer.save()
        campaign = donation.campaign
        campaign.raised_amount += donation.amount
        campaign.save()

class CampaignDonations(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [LoggedInAndReadOnly,]

    def get_queryset(self):
        campaign_id = self.kwargs['pk']
        return Donation.objects.filter(campaign_id=campaign_id)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # adjust this according to your needs
