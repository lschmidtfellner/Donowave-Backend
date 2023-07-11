from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []  # No permission for registration view

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

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

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated,]
        else:
            self.permission_classes = [AllowAny,]
        return super(CampaignViewSet, self).get_permissions()

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
