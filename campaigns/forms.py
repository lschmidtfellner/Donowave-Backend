from django import forms
from .models import Campaign, Donation

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'goal_amount', 'deadline']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
