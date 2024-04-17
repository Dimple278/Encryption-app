from django.urls import path
from cipher import views


urlpatterns = [
    path('encrypt/', views.encrypt_message, name='encrypt_message'),
    path('decrypt/', views.decrypt_message, name='decrypt_message'),
]
