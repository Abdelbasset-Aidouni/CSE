from django import forms
class CreateForm(forms.Form):
	member_name = forms.CharField()