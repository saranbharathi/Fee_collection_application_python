from django.db import models
class Students(models.Model):
    name=models.CharField(max_length=30)
    pending_fee=models.IntegerField()
    def __str__(self):
        return self.name



