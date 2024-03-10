from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    #path("sentiment/" , views.SentimentView.as_view(),name="sentiment")
    #path('profanity/' , views.ProfanityView.as_view(),name="profanity")
]