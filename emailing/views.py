from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect, Http404
from django.models import mailing

def sdml(request):
	subject = 'Orphanage Event Drive'
	message = 'Dear User,we are holding a healthcare initiative event this Sunday,at our Orphanage \n We would appreciate your presence and would request your kind contribution towards our event.'
	#from_email = settings.EMAIL_HOST_USER
	#to_list = ['shreyadesai1202@gmail.com']
	email = EmailMessage('Hello', 'World', to=['shreyadesai1202@gmail.com'])
	email.send()
	return HttpResponseRedirect('http://127.0.0.1:8000/marketing/sendmail/')