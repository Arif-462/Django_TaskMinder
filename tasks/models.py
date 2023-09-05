from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class TaskModel(models.Model):
    task_status=[
    ('Incomplete', 'Incomplete'),
    ('Complete', 'Complete'),
    ]
    
    priority_status=[
    ('0',' 0️⃣'),
    ('1',' 1️⃣'),
    ('2',' 2️⃣'),
    ('3',' 3️⃣'),
    ('4',' 4️⃣'),
    ('5',' 5️⃣'),
    ('6',' 6️⃣'),
    ('7',' 7️⃣'),
    ('8',' 8️⃣'),
    ]
    
    category=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
     
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)    
    status = models.CharField(max_length=100, choices=task_status, default='Incomplete')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=50, choices=priority_status)
    due_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=50,choices=category)
    
    def overdue(self):
        return self.due_date < now().date()
    
    
    def __str__(self):
        return self.title
  