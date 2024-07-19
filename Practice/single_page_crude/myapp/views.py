from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):
	if request.method=="POST":
		User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    role=request.POST['role'],
                )
		msg='data inserted  sucessfully'
		users = User.objects.all()
		return render(request,'index.html',{'msg':msg,'users':users})
	else:
		users = User.objects.all()
		return render(request,'index.html',{'users':users})

def delete(request,user_id):
	user = User.objects.get(id=user_id)
	if request.method=="POST":
		user.delete()
		return redirect('index')
	else:
		return render(request,'index.html',{'users':User.objects.all()})


def update(request,user_id):
		user = User.objects.get(id=user_id)
		if request.method == "POST":
			user.fname = request.POST['fname']
			user.lname = request.POST['lname']
			user.role = request.POST['role']
			user.save()
			return redirect('index')
		else:
			return render(request, 'index.html', {'user': user})






