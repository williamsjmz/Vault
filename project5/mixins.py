from django.conf import settings
import requests
import json

from django.http import JsonResponse


def FormErrors(*args):
	'''
	Handles form error that are passed back to AJAX calls
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message


def reCAPTCHAValidation(token):

	''' reCAPTCHA validation '''
	result = requests.post(
		'https://www.google.com/recaptcha/api/siteverify',
		 data={
		 	'secret': settings.RECAPTCHA_SECRET_KEY,
			'response': token
		 })

	return result.json()


class AjaxFormMixin(object):

	'''
	Mixin to ajaxify django form - can be over written in view by calling form_valid method
	'''

	# Change the result and message on success
	result = "Error"
	message = "There was an error, please try again"

	def form_invalid(self, form):
		response = super(AjaxFormMixin, self).form_invalid(form)
		if is_ajax(request=self.request):
			message = FormErrors(form)
			return JsonResponse({'result':'Error', 'message': message})
		return response

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)

		obj = form.save()
		obj.user = self.request.user
		obj.save()
		
		data = {'result': self.result, 'message': self.message}
		return JsonResponse(data)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'