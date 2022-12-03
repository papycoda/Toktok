from django.db import models

# Create your models here.

class DirectMessages(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.message