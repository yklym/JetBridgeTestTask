from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .config import default_avatar, default_description


# Create your models here.


class ViralUser(models.Model):
    invite_link = models.TextField(max_length=30)
    description = models.TextField(max_length=30, default=default_description)

    invited_users_amount = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            new_viral_user = ViralUser(user=instance, invite_link=create_ref_url(instance.username))
            new_viral_user.save()
            new_default_image = Image(viral_user=new_viral_user)
            new_default_image.save()


class Image(models.Model):
    url = models.TextField(max_length=120, default=default_avatar)
    viral_user = models.ForeignKey(ViralUser, on_delete=models.CASCADE, related_name="images", default=7)


def create_ref_url(username):
    return "--"

# post_init.connect(create_ref_url, ViralUser)
