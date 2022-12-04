from django.db import models

# Create your models here.

class DirectMessages(models.Model):
    '''A direct message object is a message sent between two users'''
    id:int = models.AutoField(primary_key=True)
    sender : any = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sender')
    receiver : any = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='receiver')
    message : str = models.CharField(max_length=50000)
    created_at : str = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.message
    
    def ComposeMsg(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.save()
        return self