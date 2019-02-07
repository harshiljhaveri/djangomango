from .models import Posts
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse


def create_post(request):
	my_form = PostForm(request.POST or None)
	if request.method == "POST":
		my_form = PostForm(request.POST)
		my_form.save()
	if my_form.is_valid():
		my_form.save()
		Posts.objects.create(my_form.cleaned_data)
	context = {
	"form": my_form
	}
	return render(request,'form.html',context)

def post_view(request):
	
	pv = Posts.objects.all()
	context = {
	"pv": pv 
	}
	return render(request,'postview.html',context)
