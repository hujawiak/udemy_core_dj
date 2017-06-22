
from django.db import models
from django.conf import settings

from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(default="My description", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class UserStripe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username
    
def stripe_callback(sender, request, user, **kwargs):
    stripe_id, created = UserStripe.objects.get_or_create(user=user)
    if created:
        print("created for  {}".format(user.username))
        
def profile_callback(sender, request, user, **kwargs):
    profile, is_created = Profile.objects.get_or_create(user=user)
    if is_created:
        profile.name = user.username
        profile.save()
    
user_logged_in.connect(stripe_callback)
user_signed_up.connect(stripe_callback)
user_signed_up.connect(profile_callback)