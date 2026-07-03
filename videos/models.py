from django.db import models


class Video(models.Model):
    video_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)  # Long Text
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )  # Foreign, nullable
    tags = gis_models.MultiPointField(null=True, blank=True)  # Multiple Point (rasmdagidek)
    date = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



