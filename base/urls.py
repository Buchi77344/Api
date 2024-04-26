from django.urls import path
from. import views

urlpatterns = [
    path('',views.CreateNote.as_view(),name ='createnote'),
    path('listnote',views.listnote),
    path('updatenote/<int:pk>/',views.updatenote),
    path('notedetails/<int:pk>/',views.notedetails),
    path('delete/<int:pk>/',views.delete),
    path('signup',views.signup.as_view()),
    path('login',views.login.as_view()),
]
   