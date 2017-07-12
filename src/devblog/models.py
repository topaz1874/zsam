from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from model_utils.models import TimeStampedModel

# Create your models here.
def upload_here(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Article(TimeStampedModel):
    title = models.CharField(max_length=512)
    tags = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=512, blank=True)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True)
    files = models.FileField(upload_to=upload_here, blank=True)
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

    # def get_markdown(self):
    #     return 
class WeightsQuerySet(models.QuerySet):
    def latest_5(self):
        return self.order_by('-created')[:5:-1]


class WeightsManager(models.Manager):
    def get_queryset(self):
        return WeightsQuerySet(self.model, using=self._db)

    def get_latest_5(self):
        return self.get_queryset().latest_5()


class Weights(models.Model):
    name = models.CharField(max_length=255)
    weights = models.DecimalField(max_digits=3,decimal_places=1)
    dates = models.DateField(auto_now=False)
    created = models.DateTimeField(auto_now_add=True)
    objects = WeightsManager()

    def __unicode__(self):
        return str(self.weights) + 'kg' + ' on ' + self.dates.strftime('%m.%d')








