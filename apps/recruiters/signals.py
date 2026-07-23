from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Recruiter


@receiver(post_save, sender=Recruiter)
def ensure_primary_recruiter(sender, instance, created, **kwargs):

    if created:

        if not Recruiter.objects.filter(
            company=instance.company,
            is_primary=True
        ).exclude(pk=instance.pk).exists():

            instance.is_primary = True
            instance.save(update_fields=["is_primary"])