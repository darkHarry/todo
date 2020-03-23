from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=100, blank=False)
    todo_done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text
