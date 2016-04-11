from django import forms
from django.contrib.auth.models import User
from book.models import UserProfile, Subscription

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-username form-control', 'placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-username form-control', 'placeholder':'Password'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-username form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-username form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-username form-control', 'placeholder':'Last name'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-username form-control', 'placeholder':'Phone'}))

	class Meta:
		model = UserProfile
		fields = ('phone',)

class SubscriptionForm(forms.ModelForm):
	CHOICES=[('Silver','Silver Package'),
			 ('Gold','Gold Package'),
			 ('Platinum','Platinum Package')]
	level = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Subscription
		fields = ('level',)
