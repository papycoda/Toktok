from django.db import models
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
    username = models.CharField(max_length=50, unique=True)
    #passwords are hashed
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

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

    

