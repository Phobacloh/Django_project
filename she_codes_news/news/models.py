from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    image_url = models.URLField(max_length=400,default="Paste image URL here")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
def publish(self):
    self.published_date = timezone.now()
    self.save()