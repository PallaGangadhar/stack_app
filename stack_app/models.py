from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    view_count = models.IntegerField(null=True, blank=True, default=0)
    answer_count = models.IntegerField(null=True, blank=True, default=0)
    score = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.question