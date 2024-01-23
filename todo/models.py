from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date 
import datetime 

class Todo(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    createdTime = models.DateField(default = datetime.date.today)
    creatorId = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = None
    )

    def timePassed(self):
        today = date.today()
        delta = today - self.createdTime
        
        return delta.days
