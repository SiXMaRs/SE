from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # หน้าเมนูหลัก
    path('register/', views.register, name='register'),  # หน้าลงทะเบียน
    path('login/', views.user_login, name='login'),  # หน้าล็อกอิน
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

]