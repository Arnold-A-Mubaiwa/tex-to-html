from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    form= PostForm()
    return render(request,'text_to_html/index.html',{'form':form})