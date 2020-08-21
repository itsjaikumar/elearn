from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update_lesson/<str:pk>/', views.updateLesson, name='update_lesson'),
    path('delete_lesson/<str:pk>/', views.deleteLesson, name='delete_lesson'),
]

