from django.db import models

# Create your models here.
class NewsQuery(models.Model):
    query = models.CharField(max_length=250, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.query

class News(models.Model):
    link = models.CharField(max_length=250, null=False, blank=False)
    headline = models.TextField()
    source = models.CharField(max_length=250, null=False, blank=False)
    query = models.ForeignKey(NewsQuery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.headline