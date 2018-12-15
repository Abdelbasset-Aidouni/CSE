from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Your user name"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Your Password"}))
class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Your user name"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form_control","placeholder":"Your Email"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Your Password"}))
	password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Confirm your password"}))

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("password must match")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if User.objects.filter(username__icontains=username).exists():
			raise forms.ValidationError("This User Name already taken")
		return username


	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email__icontains=email).exists():
			raise forms.ValidationError("Email already Registred")
		return email