from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import model1
from django.http import HttpResponse, Http404
# from django.utils import timezone
from .forms import modelform1
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app1/signup.html'


# def view4(request,post_id):
# #to make it simpler get_object404 can be used in place of try except	
# 	obj = get_object_or_404(model1,id=post_id)
# 	return HttpResponse(obj.info+" \n"+obj.title)

# def view6(request,slug):

# #to handle server errors try except is used 
# 	queryset = model1.objects.filter(slug = slug)
# 	if queryset.count() != 1:
# 		raise Http404
# 	else:	
# 		obj = queryset.first()
# 		return HttpResponse(obj)

def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}


# def view5(request,str_id):
# #to handle server errors try except is used 
#    try:
#     obj1 = model1.objects.get(title=str_id)
#    except model1.DoesNotExist:
#    	return HttpResponse("page not found") 
#    return HttpResponse(obj1.info)
#    #httpresponse take 1 argument while render take 3 arg ie request,template file,context list
'''--------------------------------------------------------------------------------------------------------------------------------'''


def list_view(request):
    qs = model1.objects.all()
    template = "app1/list.html"
    context = {"list": qs}
    return render(request, template, context)



@login_required
def create_view(request):
    # we need to use form to create objects
    form = modelform1(request.POST or None, request.FILES or None)
    print(form)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        # obj.title = form.cleaned_data.get("title")
        obj.save()

        # obj = form1.objects.create(**form.cleaned_data)
        # form = modelform1()
        return redirect("all_blogs")

    template = "form.html"
    context = {"form": form}
    return render(request, template, context)


def detail_view(request, slug):
    # to get object details
    obj = get_object_or_404(model1, slug=slug)

    template = "app1/detail.html"
    context = {"object": obj}
    return render(request, template, context)


def update_view(request, slug):
    obj = get_object_or_404(model1, slug=slug)
    obj.slug = obj.slug + '0'
    form = modelform1(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template = "form.html"
    context = {"form": form, 'title': f"Update {obj.title}"}
    return render(request, template, context)


def delete_view(request, id):
    obj = get_object_or_404(model1, pk=id)
    template = "app1/delete.html"
    context = {"object": obj}
    if request.method == 'POST':
        obj.delete()
        return redirect("/app1/")

    return render(request, template, context)

# def detail_view(request,slug):
# # to get object details
# 	try:
# 		obj = model1.objects.get(slug = slug)
# 	except model1.DoesNotExist:
# 		raise Http404
# 	except ValueError :
# 		raise Http404


# 	template = "app1/detail.html"
# 	context = {"object" : obj}
# 	return render(request,template,context)
