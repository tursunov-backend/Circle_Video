from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    parent_id = models.SmallIntegerField()
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.content[:20]}"