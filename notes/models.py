from datetime import *
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

from .managers import PublicManager

class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Topic model class.
    """

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes-topic-detail', args=((), { 'slug': self.slug}))


class Note(TimeStampedModel):
    """
    Note model class.

    A simple model to handle adding arbitrary numbers of notes to an animal profile.
    """
    topic=models.ForeignKey(Topic)
    date=models.DateField(_('Date'), default=date.today)
    content=models.TextField(_('Content'))
    public=models.BooleanField(_('Public'), default=True)
    author=models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    public_objects = PublicManager()
    objects = models.Manager()

    class Meta:
        verbose_name=_('Note')
        verbose_name_plural=_('Notes')

    def get_absolute_url(self):
        return reverse('notes-view', args=((), { 'pk': self.pk}))

