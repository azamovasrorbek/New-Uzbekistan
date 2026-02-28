from django.shortcuts import render, redirect
from .models import Comment

def home(request):
    comments = Comment.objects.all()
    return render(request, 'app/home.html', {"comments": comments})

def main(request):
    return render(request, 'app/video.html')

def add_comment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        body = request.POST.get('body')

        Comment.objects.create(name=name, body=body)

        # MUHIM: home sahifaga qaytishi kerak
        return redirect('/home/?success=1')