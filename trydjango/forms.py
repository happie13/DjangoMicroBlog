from django import forms


class ContactForms(forms.Form):

	name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget = forms.Textarea)


	def clean_email(self,*args,**kwargs):
		email  = self.cleaned_data.get("email")
		print(email)
		# if email.endswith('.com'):
		#  	raise forms.ValidationError("do not use .com its npt vloas")
		#NOT WORKING , PAGE KEEPS ON RELOADING IF VALIDATION IS REVOKED



		return email