from django.contrib.auth import login,logout,authenticate,get_user_model
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
# Create your views here.
User = get_user_model()
def home_view(request):
	
	return render(request,"base.html",{})

def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username,password=password)
		if user :
			login(request,user)
			return redirect("../")
	context = {
		"form":form,
	}
	return render(request,"login.html",context)

def logout_view(request):
	logout(request)
	return redirect("/")

def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		email = form.cleaned_data.get("email")
		user = User.objects.create_user(username, email, password)
		return redirect("/login")
	form = RegisterForm()
	context = {
		"form":form,
	}
	return render(request,"register.html",context)

