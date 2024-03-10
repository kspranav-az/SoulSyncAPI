from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    #path('profanity/' , views.ProfanityView.as_view(),name="profanity")
]