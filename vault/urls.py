
from django.urls import path

from . import views

app_name = 'vault'

urlpatterns = [
	# Template
	path('', views.AllItemsView.as_view(), name="all-items"),
	path('passwords', views.PasswordsView.as_view(), name="passwords"),
	path('notes', views.NotesView.as_view(), name="notes"),
	path('addresses', views.AddressesView.as_view(), name="addresses"),
	path('payment-cards', views.PaymentCardsView.as_view(), name="payment-cards"),
	path('bank-accounts', views.BankAccountsView.as_view(), name="bank-accounts"),

	# Create
	path('create/password', views.CreatePasswordView.as_view(), name="create_password"),
	path('create/note', views.CreateNoteView.as_view(), name="create_note"),
	path('create/address', views.CreateAddressView.as_view(), name="create_address"),
	path('create/payment-card', views.CreatePaymentCardView.as_view(), name="create_payment_card"),
	path('create/bank-account', views.CreateBankAccountView.as_view(), name="create_bank_account"),

	# Detail
	path('detail/password/<pk>', views.DetailPasswordView.as_view(), name="detail_password"),
	path('detail/note/<pk>', views.DetailNoteView.as_view(), name="detail_note"),
	path('detail/address/<pk>', views.DetailAddressView.as_view(), name="detail_address"),
	path('detail/payment_card/<pk>', views.DetailPaymentCardView.as_view(), name="detail_payment_card"),
	path('detail/bank_account/<pk>', views.DetailBankAccountView.as_view(), name="detail_bank_account"),

	# Update
	path('update/password/<int:pk>', views.UpdatePasswordView.as_view(), name="update_password"),
	path('update/note/<int:pk>', views.UpdateNoteView.as_view(), name="update_note"),
	path('update/address/<int:pk>', views.UpdateAddressView.as_view(), name="update_address"),
	path('update/payment_card/<int:pk>', views.UpdatePaymentCardView.as_view(), name="update_payment_card"),
	path('update/bank_account/<int:pk>', views.UpdateBankAccountView.as_view(), name="update_bank_account"),

	# Delete
	path('delete/password/<int:pk>', views.DeletePasswordView.as_view(), name="delete_password"),
	path('delete/note/<int:pk>', views.DeleteNoteView.as_view(), name="delete_note"),
	path('delete/address/<int:pk>', views.DeleteAddressView.as_view(), name="delete_address"),
	path('delete/payment_card/<int:pk>', views.DeletePaymentCardView.as_view(), name="delete_payment_card"),
	path('delete/bank_account/<int:pk>', views.DeleteBankAccountView.as_view(), name="delete_bank_account"),
]