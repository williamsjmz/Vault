from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from project5.mixins import AjaxFormMixin, is_ajax

from vault.models import Password, Note, Address, PaymentCard, BankAccount

from vault.forms import (
	PasswordForm, 
	NoteForm,
	AddressForm,
	PaymentCardForm,
	BankAccountForm,
)

result = "Error"
message = "There was an error, please try again"

# Create your views here.
class AllItemsView(TemplateView):
	'''
	Generic TemplateView to display all items page
	'''
	template_name = "vault/all-items.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["passwords"] = Password.objects.filter(user=self.request.user)
		context["notes"] = Note.objects.filter(user=self.request.user)
		context["addresses"] = Address.objects.filter(user=self.request.user)
		context["payment_cards"] = PaymentCard.objects.filter(user=self.request.user)
		context["bank_accounts"] = BankAccount.objects.filter(user=self.request.user)
		return context	


class PasswordsView(TemplateView):
	'''
	Generic TemplateView to display passwords page
	'''
	template_name = "vault/passwords.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["passwords"] = Password.objects.filter(user=self.request.user)
		return context	


class CreatePasswordView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for password creation
	'''

	template_name = "vault/create_item.html"
	form_class = PasswordForm
	success_url = "/"

	result = "Success"
	message = "Your password has been created successfully."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["item_name"] = "password"
		context["item_form_id"] = "passwordform"
		context["action_url"] = "/vault/create/password"
		return context		


class DetailPasswordView(DetailView):
	'''
	Generic DetailView to display details of a password.
	'''

	model = Password
	template_name = 'vault/detail_item.html'
	context_object_name = 'password'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['password'] = Password.objects.get(id=self.kwargs.get('pk'))

		return context


class UpdatePasswordView(UpdateView):
    '''
    Generic UpdateView to edit a password.
    '''

    model = Password
    fields = ['url', 'name', 'email', 'password']
    template_name = 'vault/create_item.html'
    success_url = "/vault/passwords"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_name"] = "password"
        context["update"] = True
    
        return context	


class DeletePasswordView(DeleteView):
    '''
    Generic DeleteView to delete a password.
    '''
    model = Password
    success_url ="/vault/passwords"
    template_name = "vault/delete_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = "password"
    
        return context	


class NotesView(TemplateView):
	'''
	Generic TemplateView to display notes page
	'''
	template_name = "vault/notes.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["notes"] = Note.objects.filter(user=self.request.user)
		return context	


class CreateNoteView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for note creation
	'''

	template_name = "vault/create_item.html"
	form_class = NoteForm
	success_url = "/"

	result = "Success"
	message = "Your note has been created successfully."


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["item_name"] = "note"
		context["item_form_id"] = "noteform"
		context["action_url"] = "/vault/create/note"
		return context		


class DetailNoteView(DetailView):
	'''
	Generic DetailView to display details of a note.
	'''

	model = Note
	template_name = 'vault/detail_item.html'
	context_object_name = 'note'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['note'] = Note.objects.get(id=self.kwargs.get('pk'))

		return context


class UpdateNoteView(UpdateView):
    '''
    Generic UpdateView to edit a note.
    '''

    model = Note
    fields = ['name', 'body']
    template_name = 'vault/create_item.html'
    success_url = "/vault/notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_name"] = "note"
        context["update"] = True
    
        return context	


class DeleteNoteView(DeleteView):
    '''
    Generic DeleteView to delete a note.
    '''
    model = Note
    success_url ="/vault/notes"
    template_name = "vault/delete_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = "note"
    
        return context	


class AddressesView(TemplateView):
	'''
	Generic TemplateView to display addresses page
	'''
	template_name = "vault/addresses.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["addresses"] = Address.objects.filter(user=self.request.user)
		return context	


class CreateAddressView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for address creation
	'''

	template_name = "vault/create_item.html"
	form_class = AddressForm
	success_url = "/"

	result = "Success"
	message = "Your address has been created successfully."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["item_name"] = "address"
		context["item_form_id"] = "addressform"
		context["action_url"] = "/vault/create/address"
		return context		


class DetailAddressView(DetailView):
	'''
	Generic DetailView to display details of an address.
	'''

	model = Address
	template_name = 'vault/detail_item.html'
	context_object_name = 'address'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['address'] = Address.objects.get(id=self.kwargs.get('pk'))

		return context


class UpdateAddressView(UpdateView):
    '''
    Generic UpdateView to edit an address.
    '''

    model = Address
    fields = ['name', 'title', 'first_name', 'middle_name','last_name', 
            'gender', 'birthday', 'address1', 'address2', 'address3', 'city', 
            'county', 'state', 'zip', 'country', 'email', 'phone']
    template_name = 'vault/create_item.html'
    success_url = "/vault/addresses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_name"] = "address"
        context["update"] = True
    
        return context	



class DeleteAddressView(DeleteView):
    '''
    Generic DeleteView to delete an address.
    '''
    model = Address
    success_url ="/vault/addresses"
    template_name = "vault/delete_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = "address"
    
        return context	



class PaymentCardsView(TemplateView):
	'''
	Generic TemplateView to display payment cards page
	'''
	template_name = "vault/payment_cards.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["payment_cards"] = PaymentCard.objects.filter(user=self.request.user)
		return context	


class CreatePaymentCardView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for payment card creation
	'''

	template_name = "vault/create_item.html"
	form_class = PaymentCardForm
	success_url = "/"

	result = "Success"
	message = "Your payment card has been created successfully."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["item_name"] = "payment card"
		context["item_form_id"] = "paymentcardform"
		context["action_url"] = "/vault/create/payment-card"
		return context		

class DetailPaymentCardView(DetailView):
	'''
	Generic DetailView to display details of a payment card.
	'''

	model = PaymentCard
	template_name = 'vault/detail_item.html'
	context_object_name = 'payment_card'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['payment_card'] = PaymentCard.objects.get(id=self.kwargs.get('pk'))

		return context


class UpdatePaymentCardView(UpdateView):
    '''
    Generic UpdateView to edit a payment card.
    '''

    model = PaymentCard
    fields = ['name', 'name_on_card', 'type', 'number', 'security_code', 'start_date', 'expiration_date']
    template_name = 'vault/create_item.html'
    success_url = "/vault/payment-cards"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_name"] = "payment card"
        context["update"] = True
    
        return context	



class DeletePaymentCardView(DeleteView):
    '''
    Generic DeleteView to delete a payment card.
    '''
    model = PaymentCard
    success_url ="/vault/payment-cards"
    template_name = "vault/delete_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = "payment card"
    
        return context	


class BankAccountsView(TemplateView):
	'''
	Generic TemplateView to display bank accounts page
	'''
	template_name = "vault/bank_accounts.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["bank_accounts"] = BankAccount.objects.filter(user=self.request.user)
		return context	


class CreateBankAccountView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for bank account creation
	'''

	template_name = "vault/create_item.html"
	form_class = BankAccountForm
	success_url = "/"

	result = "Success"
	message = "Your bank account has been created successfully."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["item_name"] = "bank account"
		context["item_form_id"] = "bankaccountform"
		context["action_url"] = "/vault/create/bank-account"
		return context		


class DetailBankAccountView(DetailView):
	'''
	Generic DetailView to display details of a bank account.
	'''

	model = BankAccount
	template_name = 'vault/detail_item.html'
	context_object_name = 'bank_account'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['bank_account'] = BankAccount.objects.get(id=self.kwargs.get('pk'))

		return context


class UpdateBankAccountView(UpdateView):
    '''
    Generic UpdateView to edit a bank account.
    '''

    model = BankAccount
    fields = ['name', 'bank_name', 'account_type', 'routing_name', 'account_number', 
        'swift_code', 'iban_number', 'pin', 'branch_address', 'branch_phone']
    template_name = 'vault/create_item.html'
    success_url = "/vault/bank-accounts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_name"] = "bank account"
        context["update"] = True
    
        return context	



class DeleteBankAccountView(DeleteView):
    '''
    Generic DeleteView to delete a bank account.
    '''
    model = BankAccount
    success_url ="/vault/bank-accounts"
    template_name = "vault/delete_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = "bank account"
    
        return context	