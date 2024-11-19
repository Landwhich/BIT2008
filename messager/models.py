from django.db import models

class Text(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content
