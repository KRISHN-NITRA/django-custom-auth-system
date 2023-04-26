from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    auther_name = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    def __str__(self):
        return self.auther_name
    class Meta:
        db_table = "articlemodel"
