from django.db import models


class Playlist(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="playlists")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    videos = models.ManyToManyField('videos.Video', related_name="playlists", blank=True) 

    class Meta:
        db_table = 'playlist'


    def __str__(self):
        return self.title
    

