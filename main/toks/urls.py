#urls for toks
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    #create a tok
    path('create/', create_tok),
    #list all toks by default
    path('', list_toks),
    #retrieve, update, or delete a tok
    path('<int:pk>/', tok_detail),
]