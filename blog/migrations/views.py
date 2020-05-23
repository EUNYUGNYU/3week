from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog



def home(request):
    blogs= Blog.objects 
    return render(request, 'home.html', {'blogs': blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) #이용자가 원하는 몇번 객체를 나타내는 함수
    return render(request,'detail.html', {'blog':blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog= Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date = timezone.datetime.now() #시점
    blog.save() #객체.save() - 저장하는 메소드, (delete는 삭제)
    return redirect('/blog/'+str(blog.id)) #처리후 (url)로 넘어가시오