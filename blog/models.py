from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title