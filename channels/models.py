from django.db import models


class Channel(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="channels")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'channels'


    def __str__(self):
        return self.name
    

