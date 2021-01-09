from django.shortcuts import render

# Create your views here.
from .models import SearchQuery


def search_view(request):
	query  = request.GET.get('q',None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	if query is  not None:
		SearchQuery.objects.create(user= user,query=query)	

	context = {"query":query}
	template = 'search/views.html'
	return render(request,template,context)