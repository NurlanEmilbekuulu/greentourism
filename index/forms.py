from django import forms
from blog.models import Subscriber
from book.models import BookingTour, BookingRoom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.Form):
	fname = forms.CharField(widget=forms.TextInput(attrs={'id' : 'fname','class' : 'form-control'}))
	lname = forms.CharField(widget=forms.TextInput(attrs={'id' : 'lname','class' : 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'email','class' : 'form-control'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'id' : 'subject','class' : 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'id' : 'message', 'class' : 'form-control', 'cols' : '30', 'rows' : '10'}))

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ('email',)

		widgets = {
			'email' : forms.EmailInput(attrs={'id' : 'email','class' : 'form-control', 'placeholder' : 'Enter your email'})
		}

class BookingTourForm(forms.ModelForm):

	class Meta:
		model = BookingTour

		fields = ('check_in', 'check_out', 'adults', 'children',)

		widgets = {
			'check_in' : forms.TimeInput(attrs={'class':'form-control date', 'id':'date id_check_in', 'autocomplete':'off'}),
			'check_out' : forms.TimeInput(attrs={'class':'form-control date', 'id':'date id_check_out', 'autocomplete':'off'}),
			'adults' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '0'}),
			'children' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '0'}),
		}


class BookingRoomForm(forms.ModelForm):

	class Meta:
		model = BookingRoom

		fields = ('check_in', 'check_out', 'rooms', 'adults', 'children',)

		widgets = {
			'check_in' : forms.TimeInput(attrs={'class':'form-control date', 'id':'date id_check_in', 'autocomplete':'off'}),
			'check_out' : forms.TimeInput(attrs={'class':'form-control date', 'id':'date id_check_out', 'autocomplete':'off'}),
			'rooms' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '0'}),
			'adults' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '0'}),
			'children' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '0'}),
		}

class UserRegistrationForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'email address'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'password confirm'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'password'}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)

			if not user:
				raise forms.ValidationError('This user does not exist')

			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')

			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)