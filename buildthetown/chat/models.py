from django.db import models

# Create your models here.
class Message(models.Model): 
    content = models.TextField()
    sendet_by = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.content[:20]}..."