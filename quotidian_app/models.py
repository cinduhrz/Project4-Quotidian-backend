from django.db import models

# Create your models here.
class Todo(models.Model):
    # auto sets date field to when object is first created
    date = models.DateField(auto_now_add=True)
    
    # actual text of todo
    description = models.CharField(max_length=100)
    
    # todo can fall into 3 categories: event, task, and reminder (backburner tasks)
    category = models.CharField(max_length=25)
    
    # status only exists for todos in the task category, and there are 3 possible values: unfinished, finished, and cancelled (this doesn't remove the todo from the database, unlike deleting it does. it simply crosses it out).
    # for todos in event and reminder category, status will be null
    status = models.CharField(max_length=25, null=True)