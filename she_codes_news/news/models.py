from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wired.com%2Fstory%2Fcats-australia-bushfires%2F&psig=AOvVaw0dcvs9cBr93XtPoiVwHnVo&ust=1596340320650000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPitg6CN-eoCFQAAAAAdAAAAABAD")
