
from django.urls import path

from . import views

app_name = 'password'

urlpatterns = [
	# Template
	path('generator/', views.password_generator, name="password_generator"),
]