from random import choices
from django import forms
from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget

from .models import (
    Password, 
    Note, 
    Address, 
    PaymentCard, 
    BankAccount
)


class PasswordForm(ModelForm):
	'''
	Form to create a password
	'''
	url = forms.URLField(required=True, widget=forms.URLInput(attrs={'placeholder': '*Site URL...'}))
	name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name for this password...'}))
	email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': '*Email...'}))
	password = forms.CharField(max_length=25, required=True,
		widget=forms.PasswordInput(attrs={'placeholder': '*Site password..','class':'password', 'id': 'password-container'}))

	class Meta:
		model = Password
		fields = ('url', 'name', 'email', 'password', )


class NoteForm(ModelForm):
    '''
    Form to create a note
    '''

    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name for this note...'}))
    body = forms.CharField(max_length=500, required=True,
        widget=forms.Textarea(attrs={'placeholder': '*Note\'s body...', 'class': 'text-input'}))

    class Meta:
        model = Note
        fields = ('name', 'body')


class AddressForm(ModelForm):
    '''
    Form to create an address
    '''
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name for this address...'}))
    title = forms.ChoiceField(required=False, choices=Address.TITLE_CHOICES, widget=forms.Select(attrs={'style': 'border: 1px solid !important;'}))
    first_name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*First name...'}))
    middle_name = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Middle name...'}))
    last_name = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Last name...'}))
    gender = forms.ChoiceField(choices = Address.GENDER_CHOICES, required=False, widget=forms.Select(attrs={'style': 'border: 1px solid !important;'}))
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'style': 'border: 1px solid !important;'}))
    address1 = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': '*Address 1...'}))
    address2 = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Address 2...'}))
    address3 = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Address 3...'}))
    city = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'City...'}))
    county = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'County...'}))
    state = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'State...'}))
    zip = forms.CharField(max_length=5, required=False, widget=forms.TextInput(attrs={'placeholder': 'ZIP Code...'}))
    country = CountrySelectWidget()
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    phone = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone number...'}))

    class Meta:
        model = Address
        fields = ('name', 'title', 'first_name', 'middle_name','last_name', 
            'gender', 'birthday', 'address1', 'address2', 'address3', 'city', 
            'county', 'state', 'zip', 'country', 'email', 'phone')


class PaymentCardForm(ModelForm):
    '''
    Form to create a payment card
    '''
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name for this payment card...'}))
    name_on_card = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name on card...'}))
    type = forms.ChoiceField(required=False, choices=PaymentCard.TYPE_CHOICES, widget=forms.Select(attrs={'style': 'border: 1px solid !important;'}))
    number = forms.CharField(max_length=19, required=True, widget=forms.TextInput(attrs={'placeholder': '*Card number...'}))
    security_code = forms.CharField(max_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': '*Security code (3 digits)...'}))
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'style': 'border: 1px solid !important;'}))
    expiration_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'style': 'border: 1px solid !important;'}))

    class Meta:
        model = PaymentCard
        fields = ('name', 'name_on_card', 'type', 'number', 'security_code', 'start_date', 'expiration_date')


class BankAccountForm(ModelForm):
    '''
    Form to create a bank account
    '''

    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Name for this bank account...'}))
    bank_name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Bank name...'}))
    account_type = forms.ChoiceField(choices=BankAccount.TYPE_CHOICES, required=False, widget=forms.Select(attrs={'style': 'border: 1px solid !important;'}))
    routing_name = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Routing name...'}))
    account_number = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': '*Account number...'}))
    swift_code = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'SWIFT Code...'}))   
    iban_number = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'IBAN Number...'}))
    pin = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'PIN Number...'}))
    branch_address = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Branch address...'}))
    branch_phone = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Branch phone number...'}))

    class Meta:
        model = BankAccount
        fields = ('name', 'bank_name', 'account_type', 'routing_name', 'account_number', 
        'swift_code', 'iban_number', 'pin', 'branch_address', 'branch_phone')