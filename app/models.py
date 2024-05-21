from django.db import models

class Task(models.Model):
    task=models.CharField( max_length=250)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.task
