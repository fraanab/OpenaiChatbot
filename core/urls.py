from django.urls import path
from .views import main, chatbot

urlpatterns = [
	path('', main, name='main'),
	path('chat/', chatbot, name='chatbot')
]