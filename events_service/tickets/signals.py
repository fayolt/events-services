from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from rest_framework import serializers

from .models import Ticket, TicketType


@receiver(pre_save, sender=Ticket)
def validate_ticket_emition(
        sender, instance, raw, using, update_fields, **kwargs):
    query = Ticket.objects.filter(seat=instance.seat)
    if query.filter(tickettype__date=instance.tickettype.date).exists():
        raise serializers.ValidationError(
            {'seat': ['Ticket already emitted for this seat', ]}
        )


@receiver(pre_save, sender=TicketType)
def create_slug(sender, instance, raw, using, update_fields, **kwargs):
    if not instance.id:
        instance.slug = slugify(instance.name)
