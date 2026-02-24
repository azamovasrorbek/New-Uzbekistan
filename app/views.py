from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def main(request):
    return render(request, 'app/video.html')
