from django.shortcuts import redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from project5.mixins import(
	AjaxFormMixin, 
	reCAPTCHAValidation,
	FormErrors,
	is_ajax,
)

from .forms import (
	UserForm,
	AuthForm,
)

result = "Error"
message = "There was an error, please try again"

class AccountView(TemplateView):
	'''
	Generic TemplateView to display user account page
	'''
	template_name = "users/account.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class SignUpView(AjaxFormMixin, FormView):
    '''
    Generic FormView with our mixin for user sign-up with
    '''

    template_name = "users/sign_up.html"
    form_class = UserForm
    success_url = "/"

    # reCAPTURE key required in context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context

	# Over write the mixin logic to get, check and save reCAPTURE score
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if is_ajax(request=self.request):
            
            token = form.cleaned_data.get('token')
            captcha = reCAPTCHAValidation(token)
            if captcha["success"]:
                obj = form.save()
                obj.email = obj.username
                obj.save()
				
                login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				# Change result & message on success
                result = "Success"
                message = "Thank you for signing up"
			
            data = {'result': result, 'message': message}
            return JsonResponse(data)

        return response


class SignInView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for user sign-in
	'''

	template_name = "users/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if is_ajax(request=self.request):
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			# Attempt to authenticate user
			user = authenticate(self.request, username=username, password=password)
			if user is not None:
				login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
				result = "Success"
				message = 'You are now logged in'
			else:
				message = FormErrors(form) 
			data = {'result': result, 'message': message}
			return JsonResponse(data)
		return response




def sign_out(request):
	'''
	Basic view for user sign out
	'''
	logout(request)
	return redirect(reverse('users:sign-in'))