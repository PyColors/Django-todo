from django.db import models

# Todo models
class Todo(models.Model):
  name = models.CharField(max_length=100)
  due_date = models.DateField()

  # Given a name to a model with: __str__ method
  # string representation of the model

  # self.name return name of todo that has been created
  def __str__(self):
    return self.name