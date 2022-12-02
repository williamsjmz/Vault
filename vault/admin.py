from django.contrib import admin
from .models import Password, Note, Address, PaymentCard, BankAccount

# Register your models here.
admin.site.register(Password)
admin.site.register(Note)
admin.site.register(Address)
admin.site.register(PaymentCard)
admin.site.register(BankAccount)