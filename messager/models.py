import os
import django
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank=True, symmetrical=True)
    bio = models.TextField(max_length=500, blank=True, default="I HAVE NOTTTING!!!")
    pfimage = models.ImageField(upload_to='media/', default="NA")
    pfp = ImageSpecField(
        source='pfimage',
        processors=[ResizeToFit(100, 100)],
        format='PNG',
        options={'quality': 70},
    )

    def add_friend(self, friend_user):
        self.friends.add(friend_user)
        friend_user.friends.add(self)

    def remove_friend(self, friend_user):
        self.friends.remove(friend_user)
        friend_user.friends.remove(self)

# class Room(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name

class Text(models.Model):
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='texts', default=None)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    sender = models.ForeignKey(Profile, related_name="send", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="receive", on_delete=models.CASCADE)

    def __str__(self):
        return "f sender:{self.sender} receiver:{self.receiver}, {self.content} - {self.date}"