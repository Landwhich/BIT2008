from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Text(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='texts', default=None)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return "f{self.room}: {self.content}"