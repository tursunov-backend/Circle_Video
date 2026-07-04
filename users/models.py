from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  

    def __str__(self):
        return self.first_name

