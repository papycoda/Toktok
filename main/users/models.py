import datetime
from typing import Union
import uuid
from django.core.files import File
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.dispatch import receiver
from fastapi.responses import JSONResponse
from django.db.models.signals import post_save
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ValidationError
import shortuuid

def generate_uuid():
    '''This generates a unique userid for each user'''
    return shortuuid.ShortUUID().random(length=10)

app = FastAPI()

# define request and response models for the endpoint
class UserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: uuid
    username: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

class User(models.Model):
    id = models.CharField(
        max_length=30,
        primary_key=True,
        default=generate_uuid,
        editable=False
    )
    # usernames are unique
    username = models.CharField(max_length=50, unique=True)
    # passwords are hashed
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def validate_user_request(user_request: UserRequest):
        # validate the email field
        try:
            user_request.email.validate()
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
        # check if the username and password are at least 6 characters long
        if len(user_request.username) < 6 or len(user_request.password) < 6:
            raise HTTPException(status_code=400, detail="Username and password must be at least 6 characters long")
        # check if the first and last name are at least 2 characters long
        if len(user_request.first_name) < 2 or len(user_request.last_name) < 2:
            raise HTTPException(status_code=400, detail="First and last name must be at least 2 characters long")
    
    def CreateAccount(self, username: str, password: str, email: str, first_name: str, last_name: str):
        if not (username and password and email and first_name and last_name):
            return JSONResponse(status_code=400, content={"error": "Invalid input"})

        self.username = username
        self.password = make_password(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        # validate the user and save the user
        if username and password and email and first_name and last_name:
            self.save()
            return self
        else:
            return None

    
    def Follow(self, user: 'User'):
        profile = self.profile
        if user not in profile.follows.all():
            profile.follows.add(user)
            profile.save()

    def Unfollow(self, user: 'User'):
        profile = self.profile
        if user in profile.follows.all():
            profile.follows.remove(user)
            profile.save()

    
    def Block(self, user: 'User'):
        profile = self.profile
        if user not in profile.blocked.all():
            profile.blocked.add(user)
            profile.save()

    def Unblock(self, user: 'User'):
        profile = self.profile
        if user in profile.blocked.all():
            profile.blocked.remove(user)
            profile.save()


    

class Profile(models.Model):
    '''a profile object is a user's profile, it would have a user field, a follows field and a following field'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='following', blank=True, symmetrical=False)
    blocked = models.ManyToManyField(User, related_name='blocked_by', blank=True, symmetrical=False)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


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
    

    def EditProfile(self, bio: str, profile_pic: Union[str, File]):
        if bio and len(bio) <= 500:
            self.bio = bio
        if profile_pic and isinstance(profile_pic, (str, File)):
            self.profile_pic = profile_pic
        self.save()


    

