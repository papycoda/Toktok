from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver

import shortuuid

# Create your models here.

#user model for every person on the app.
def generate_uuid():
    '''This generates a unique userid for each user'''
    return shortuuid.ShortUUID().random(length=10)

class User(models.Model):
    id = models.CharField(
        max_length=30,
        primary_key=True,
        default=generate_uuid,
        editable=False
    )
    #usernames are unique
    username : str = models.CharField(max_length=50, unique=True)
    #passwords are hashed
    password : str = models.CharField(max_length=100)
    email : str = models.EmailField(max_length=100)
    first_name : str = models.CharField(max_length=50)
    last_name : str = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    def CreateAccount(self, username, password, email, first_name, last_name):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        #validate the user, hash the password, and save the user
        if username and password and email and first_name and last_name:
            password = make_password(password)
            self.save()
            return self
        else:
            return None

    def Login(self, username, password):
        #validate the user, hash the password, and save the user
        if username and password:
            password = make_password(password)
            self.save()
            return self
        else:
            return None

    def Logout(self):
        pass
    
    def Follow(self, user):
        pass

    def Unfollow(self, user):
        pass
    
    def Block(self, user):
        pass
    
    def Unblock(self, user):
        pass
    

class Profile(models.Model):
    '''a profile object is a user's profile, it would have a user field, a follows field and a following field'''
    #count the number of follows
    def num_follows(self):
        return self.follows.all().count()

        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='following', blank=True, symmetrical=False)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    followers_count = property(num_follows)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def Create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
            #user automatically follows themselves
            user_profile.follows.add(instance)
            user_profile.save()
    

    def EditProfile (self, bio, profile_pic):
        self.bio = bio
        self.profile_pic = profile_pic
        self.save()
        return self

    

