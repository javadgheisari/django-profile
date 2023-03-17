from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True, null=True, default='')

    def __str__(self) -> str:
        return self.title
