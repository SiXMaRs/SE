from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'ชื่อผู้ใช้นี้ถูกใช้แล้ว'})

        # สร้าง User และ UserProfile พร้อมวันเกิด
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, date_of_birth=datetime.strptime(date_of_birth, '%Y-%m-%d'))
        return redirect('register')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:  # ตรวจสอบความถูกต้อง
            login(request, user)
            return redirect('profile')  # ไปหน้าโปรไฟล์
        else:
            return render(request, 'login.html', {'error': 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def main_page(request):
    return render(request, 'main.html')


def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

@login_required
def profile(request):
    try:
        profile = request.user.userprofile  # ดึง UserProfile ที่สัมพันธ์กับ User
        context = {
            'profile': profile,
            'age': profile.age,  # ใช้ property `age` จาก model
        }
    except UserProfile.DoesNotExist:
        context = {
            'error': "โปรไฟล์ของคุณยังไม่ถูกสร้าง",
        }
    return render(request, 'profile.html', context)