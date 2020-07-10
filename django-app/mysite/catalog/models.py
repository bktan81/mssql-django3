from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Tag(models.Model):
    STATUS_ACTIVE = 'ACTIVE'
    STATUS_INACTIVE = 'INACTIVE'

    STATUS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    )

    tag_address = models.CharField(_('Address'), max_length=140)
    description = models.TextField(_('Description'), default='', blank=True)
    status = models.CharField(blank=True, max_length=10, choices=STATUS, default=STATUS_ACTIVE)
    last_seen = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        verbose_name = _('Tag')

    def __str__(self):
        return self.tag_address+"/"+self.description