from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Campaign, Donation, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('metamask_wallet_address',)

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'userprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.is_staff = True
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id', 'title', 'description', 'goal_amount', 'deadline', 'category',
            'raised_amount', 'web3_raised_amount', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(CampaignSerializer, self).create(validated_data)


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'  # or list the field names if you want to be selective
