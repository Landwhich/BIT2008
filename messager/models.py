from django.db import models
from django.contrib.auth.models import AbstractUser

# class AltUser(AbstractUser):
#     friends = models.ManyToManyField("self", blank=True)
#
#     def add_friend(self, friend_user):
#         self.friends.add(friend_user)
#         friend_user.friends.add(self)
#
#     def remove_friend(self, friend_user):
#         self.friends.remove(friend_user)
#         friend_user.friends.remove(self)

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
    # sender = models.ForeignKey(AltUser, related_name="sender" ,on_delete=models.CASCADE, default=None)
    # receiver = models.ForeignKey(AltUser, related_name="receiver", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "f{self.content}, {self.date}"
        # return "f sender:{self.sender} receiver:{self.receiver}, {self.content} - {self.date}"