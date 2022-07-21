from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=150)
    published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title