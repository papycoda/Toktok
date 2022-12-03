from django.db import models

from users.models import User
from users.models import generate_uuid as generate_uuid

# Create your models here.

class Toks(models.Model):
    '''a toks object is an object similar to a tweet, it would have an id field, a created by field, a likes field and a retweet field'''
    id = models.CharField(
        max_length=30,
        primary_key=True,
        default=generate_uuid,
        editable=False
    )
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

class TokComment(models.Model):
    '''comments under a tok, details include the user who commented, the tok commented on and the comment'''
    # the user who commented
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # the tok commented on
    tok = models.ForeignKey(Toks, on_delete=models.CASCADE)
    # the comment
    comment = models.CharField(max_length=500)
    #likes for comments
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    #retweets for comments
    retoks = models.ManyToManyField(User, related_name='comment_retoks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment     
    
    class Meta:
        ordering = ['-created_at']

class TokCommentReply(models.Model):
    '''replies to a comment, details include the user who replied, the comment replied to and the reply'''
    # the user who replied
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # the comment replied to
    comment = models.ForeignKey(TokComment, on_delete=models.CASCADE)
    # the reply
    reply = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply

    class Meta:
        ordering = ['-created_at']
# to do --- link the toks comments to the toks model and the toks comments replies to the toks comments model  in admin.py
# to do --- add a field to the toks model to count the number of comments and replies

