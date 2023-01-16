from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Post)
def remove_is_main(sender, created, instance, **kwargs):
    if created:
        if sender.is_main == True:
            post = models.Post.objects.filter(is_main=True).first()
            if post is not None:
                post.is_main = False
                post.save()
            else:
                pass


@receiver(pre_save, sender=models.Post)
def remove_is_main_save(sender, instance, **kwargs):
    if instance.is_main:
        post = models.Post.objects.filter(is_main=True).first()
        if post is not None:
            post.is_main = False
            post.save()
        else:
            pass

