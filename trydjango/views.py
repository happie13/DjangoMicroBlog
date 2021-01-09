from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from .forms import ContactForms


def homepage(request):
	return render(request,"base.html",)

@login_required
def contact(request):
	form = ContactForms(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	
	form = ContactForms()	
	context = {"title":"contact us",
				'form':form}		
	return render(request,"form.html",context)
	#return HttpResponse(get_template("form.html" ).render({"title":'contact us'}))


def about(request):
	template_name = "base.html"
	context  = {"title":"hope its working","text2":"let's do it "}
	template_obj = get_template(template_name)
	return HttpResponse(template_obj.render(context))



def login(request):
	return render(request, 'login.html')

