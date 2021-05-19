from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Title = models.CharField(max_length=20)
    Info = models.TextField()
    Date = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = ()
        ordering = ["-Title"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])
class Comm(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.CharField(max_length=20,editable=False)
    class Meta:
        permissions = ()
        ordering = ["-date"]
    def publish(self):
        self.published_date = timezone.now()
        self.save()