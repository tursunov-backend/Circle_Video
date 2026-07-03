from django.db import models

class Video(models.Model):
    video_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True) 
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="videos"
    )
    tags = models.ManyToManyField("Tag", related_name="videos", blank=True) 
    date = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



