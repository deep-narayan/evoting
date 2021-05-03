from django.shortcuts import render
from .models import UserProfile,ip
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

f=0
v=0

def checkip(request):
	add=request.META.get('REMOTE_ADDR')
	p=ip.objects.all()
	for i in p:
		if i.ipaddress == add:
			global f
			f=1
		else:
			f=0
	try:
		z=ip(ipaddress=add)
		z.save()
	except:
		return render(request,'err.html',{'err':"You have Already voted!!! Let Other's Vote "})


def home(request):
	try:
		global f
		global v
		if f==0:
			u=UserProfile.objects.all()
			if request.method=='POST':
				uo=request.POST['uid']
				v=UserProfile.objects.filter(id=uo)
				#print(v[0].name)
				newvote=int(v[0].vote+1)
				v.update(vote=newvote)
				checkip(request)
				return render(request,'voted.html')
			return render(request,'index.html',{'us':u})

		elif f==1:
			print(v[0].name)
			newvote=int(v[0].vote-1)
			v.update(vote=newvote)

			return render(request,'err.html',{'err':"You have Already voted!!!Let Other's Vote "})
	except:
		return render(request,'err.html',{'err':"No User Found, Candidate Should get enrolled "})
	return render(request,'index.html')


	



def details(request,id):
	#print(id)
	try:
		u=UserProfile.objects.get(id=id)
		#print(u)
	except:
		return render(request,'err.html',{'err':"No User Found"})
	#print(u)
	return render(request,'details.html',{'z':u})

