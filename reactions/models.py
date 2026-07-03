from django.db import models


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"{self.user} likes {self.video}"


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dislikes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="dislikes")

    def __str__(self):
        return f"{self.user} dislikes {self.video}"



class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="views")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="views")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.video}"
