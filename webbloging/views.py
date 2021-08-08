from django.shortcuts import render,redirect
from blog.models import publishedblog
from userprofile.models import User_profileing
import random


def home(request):
	try:
		pb=publishedblog.objects.all().last()
		nnb1= publishedblog.objects.all()
		#print(nb1)
		nb1=nnb1[2]
		nnb2= publishedblog.objects.all()
		nb2=nnb2[3]
		#print(nb2)
		nnb3= publishedblog.objects.all()
		nb3=nnb3[4]
		#print(nb3)
	except:
		return render(request,'error.html')

	try:
		uobj=User_profileing.objects.get(username=request.user.username)
		u=uobj.username
	except:
		u=""
		
	return render(request,'index.html',{'lblog':pb,'nb1':nb1,'nb2':nb2,'nb3':nb3,'user':u})