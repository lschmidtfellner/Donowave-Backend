# serializers.py in your campaigns app

from rest_framework import serializers
from .models import Campaign, Donation

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'  # or list the field names if you want to be selective

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'  # or list the field names if you want to be selective