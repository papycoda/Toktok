from django.db import models

from users.models import User

# Create your models here.

class Toks(models.Model):
    '''a toks object is an object similar to a tweet, it would have an id field, a created by field, a likes field and a retweet field'''
    id = models.IntegerField(primary_key=True)
    # the user who created the toks
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # the toks text
    tok = models.CharField(max_length=500)
    # the toks likes
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # the toks retoks
    retoks = models.ManyToManyField(User, related_name='retoks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    #comment section
    class Meta:
        ordering = ['-created_at']    

    def __str__(self):
        return self.tok
    #count the number of likes
    def num_likes(self):
        return self.likes.all().count()
    #count the number of retoks
    def num_retoks(self):
        return self.retoks.all().count()
    