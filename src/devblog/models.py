from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from model_utils.models import TimeStampedModel

# Create your models here.
class Article(TimeStampedModel):
    title = models.CharField(max_length=512)
    tags = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=512, blank=True)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)
    #create
    #modified

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        # todo clean title method to valid same slug         
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('devblog:detail', kwargs={'slug':self.slug})