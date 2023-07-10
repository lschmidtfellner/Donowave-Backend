from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    metamask_wallet_address = models.CharField(max_length=42)

    def __str__(self):
        return self.user.username

class Campaign(models.Model):
    CATEGORY_CHOICES = [
        ('AN', 'Animals'),
        ('BU', 'Business'),
        ('CO', 'Community'),
        ('CR', 'Creative'),
        ('ED', 'Education'),
        ('EM', 'Emergencies'),
        ('EN', 'Environment'),
        ('EV', 'Events'),
        ('FA', 'Faith'),
        ('FM', 'Family'),
        ('FN', 'Funeral & Memorial'),
        ('MD', 'Medical'),
        ('MB', 'Monthly Bills'),
        ('NW', 'Newlyweds'),
        ('OT', 'Other'),
        ('SP', 'Sports'),
        ('TR', 'Travel'),
        ('UR', 'Ukraine Relief'),
        ('VO', 'Volunteer'),
        ('WI', 'Wishes'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=15, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='OT')

    def __str__(self):
        return self.title

    def is_completed(self):
        return self.raised_amount >= self.goal_amount

    def is_expired(self):
        return self.deadline < timezone.now()


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} to {self.campaign.title}'
