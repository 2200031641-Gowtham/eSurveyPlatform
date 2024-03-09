from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='user_index'),
    path('create_form',views.create_form,name='create_form'),
    path('add_question',views.add_question,name='add_question'),
    path('save_user',views.save_user,name='save_user'),
]