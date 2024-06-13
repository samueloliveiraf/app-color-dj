from django.db import models


class Item(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
    def status_color(self):
        colors = {
            'New': '#42c2f5',
            'In Progress': '#4287f5',
            'Completed': '#42f587'
        }
        return colors.get(self.status, '#000000')
