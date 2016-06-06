from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="...")    
    text = tinymce_models.HTMLField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def defaultimage(self):
    	self

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
