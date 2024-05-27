from django.db import models
from django_quill.fields import QuillField
from django.template.defaultfilters import truncatechars

class Keyword(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=256)
    description = QuillField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True, null=True, default='')
    keywords = models.ManyToManyField(Keyword)

    def __str__(self) -> str:
        return self.title
    
    @property
    def short_description(self):
        return truncatechars(self.description.plain, 100)
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"