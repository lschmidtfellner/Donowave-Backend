# views.py in your campaigns app
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class UserCreate(APIView):

    def post(self, request, format='json'):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
