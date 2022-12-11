#urls.py
# Path: main\users\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    #user list
    path('', views.user_list, name='user_list'),
    #user detail uing id
    path('<str:id>/', views.user_detail, name='user_detail'),
    #user detail using username
    path('<str:username>/', views.user_by_username, name='user_by_username'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:id>/', views.profile, name='profile'),
    # path('profile/<int:id>/follow/', views.follow, name='follow'),
    # path('profile/<int:id>/unfollow/', views.unfollow, name='unfollow'),
    # path('profile/<int:id>/block/', views.block, name='block'),
    # path('profile/<int:id>/unblock/', views.unblock, name='unblock'),
    # path('profile/<int:id>/edit/', views.edit, name='edit'),
    # path('profile/<int:id>/delete/', views.delete, name='delete'),
    # path('profile/<int:id>/followers/', views.followers, name='followers'),
    # path('profile/<int:id>/following/', views.following, name='following'),
    # path('profile/<int:id>/blocked/', views.blocked, name='blocked'),
    # path('profile/<int:id>/toks/', views.toks, name='toks'),
    # path('profile/<int:id>/toks/<int:tok_id>/', views.toks, name='toks'),
    # path('profile/<int:id>/toks/<int:tok_id>/delete/', views.delete_tok, name='delete_tok'),
    # path('profile/<int:id>/toks/<int:tok_id>/like/', views.like, name='like'),
    # path('profile/<int:id>/toks/<int:tok_id>/unlike/', views.unlike, name='unlike'),
    # path('profile/<int:id>/toks/<int:tok_id>/retok/', views.retok, name='retok'),

]

    
