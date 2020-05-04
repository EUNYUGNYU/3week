from django.shortcuts import render
from .models import Blog



def main(request):
    blogs = Blog.objects #쿼리셋 #메소드
    return render(request, 'main.html', {'blogs': blogs})