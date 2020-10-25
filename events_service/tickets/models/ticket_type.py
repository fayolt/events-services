from django.db import models
from django.template.defaultfilters import slugify

from . import Date, Timestamp


class TicketType(Timestamp):

    class Meta:
        unique_together = ('date', 'slug')

    name = models.CharField(max_length=20)
    slug = models.SlugField(allow_unicode=True, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.ForeignKey(
        Date, related_name="ticket_types", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.name.lower()
            self.slug = slugify(self.name)

        super(TicketType, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name.title()} {self.price}"
