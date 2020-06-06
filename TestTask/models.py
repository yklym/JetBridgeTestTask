from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .config import default_avatar


# Create your models here.


class Image(models.Model):
    url = models.TextField(max_length=120, default=default_avatar)


class ViralUser(models.Model):
    invite_link = models.TextField(max_length=30)
    description = models.TextField(max_length=30, default="")

    invited_users_amount = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="profile")

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            new_viral_user = ViralUser(user=instance,
                                       invite_link=create_ref_url(instance.username),
                                       images=Image.objects.create())
            new_viral_user.save()
        # print(instance)
        # instance.profile.save()


def create_ref_url(username):
    return "--"

# post_init.connect(create_ref_url, ViralUser)
