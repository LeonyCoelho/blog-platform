from django.shortcuts import render

def new_post(request):
    return render(request, 'new_post.html')