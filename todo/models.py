from django.db import models

# Create your models here.

# ('CSSに渡される値', '管理画面上に表示される値')
PRIORITY = (('danger', 'high'), ('success', 'normal'), ('info', 'low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title
