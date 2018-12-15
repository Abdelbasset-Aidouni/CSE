from django.shortcuts import render
from django.http import JsonResponse
from members.forms import CreateForm
from members.models import Member
# Create your views here.
def create_or_retrieve(request,pk=None):
	if pk:
		member = Member.objects.filter(pk=pk)
		if member:
			return JsonResponse({ "member_name":member.member_name ,})
		return JsonResponse({"error":"member Doesnt exist"})
	else:
		if request.method == "POST":
			form = CreateForm(request.POST or None)
			if form.is_valid():
				member_name = form.cleaned_data.get("member_name")
				if member_name:
					Member.objects.create(member_name=member_name)
					return JsonResponse({ "member_name":member_name ,})
		else:
			member_list = Member.objects.all()
			return JsonResponse({ "members":[x.member_name for x in member_list]})
	return None

def retrieve_member(request,pk):
	pass

def delete_member(request,pk=None):
	if pk:
		member = Member.objects.filter(id=pk)
		if member :
			member.delete()
			return JsonResponse({ "status":"Deleted Succesfuly"})

def update_member(request,pk):
	form = CreateForm(request.POST or None)
	if form.is_valid():
		member_name = form.cleaned_data.get("member_name")
		obj = Member.objects.get(pk=pk)
		obj.member_name = member_name
		obj.save()
		return JsonResponse({ "status":"Deleted Succesfuly"})