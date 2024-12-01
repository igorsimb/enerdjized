from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user)


@receiver(pre_save, sender=User)
def lower_case_username(sender, instance, **kwargs):
    """
    Convert username to lowercase.
    """
    if instance.username:
        instance.username = instance.username.lower()
