from django.db import models

# Create your models here.

class News(models.Model):
    link = models.CharField(max_length=250, null=False, blank=False)
    headline = models.TextField()
    source = models.CharField(max_length=250, null=False, blank=False)
    query = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.headline