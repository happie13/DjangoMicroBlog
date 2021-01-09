from django import forms
from .models import model1

class form1(forms.Form):

	title = forms.CharField()
	slug = forms.SlugField()
	info  = forms.CharField(widget= forms.Textarea)

class modelform1(forms.ModelForm):
	class Meta:
		model = model1
		fields = ['title','image','slug','info']


