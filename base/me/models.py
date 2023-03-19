from django.db import models
from django_quill.fields import QuillField
from django.template.defaultfilters import truncatechars


class Blog(models.Model):
    title = models.CharField(max_length=256)
    description = QuillField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True, null=True, default='')

    def __str__(self) -> str:
        return self.title
    
    @property
    def short_description(self):
        return truncatechars(self.description.plain, 100)
