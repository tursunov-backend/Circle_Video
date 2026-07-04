from django.db import models

class Video(models.Model):
    video_url = models.FileField(upload_to="videos/")
    title = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True) 
    category = models.IntegerField()
    tags = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey('channels.Channel', on_delete=models.CASCADE, related_name="videos")

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="likes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user} likes {self.video}"


class Dislike(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="dislikes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="dislikes")

    def __str__(self):
        return f"{self.user} dislikes {self.video}"


class View(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="views")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="views")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.video}"
