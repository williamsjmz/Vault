from django.db import models
from django_countries.fields import CountryField
from users.models import User

# Create your models here.
class Password(models.Model):
    '''
    Model for storing passwords.
    '''

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="passwords")

    url = models.URLField(verbose_name="URL", blank=True, null=True)
    name = models.CharField(verbose_name="Site name", max_length=25, blank=True, null=True)
    email = models.EmailField(verbose_name="Email", max_length=100, blank=True, null=True)
    password = models.CharField(verbose_name="Password", max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.user}: {self.name}'

class Note(models.Model):
    '''
    Model for storing notes.
    '''

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="notes")

    name = models.CharField(verbose_name="Note name", max_length=25, blank=True, null=True)
    body = models.TextField(verbose_name="Note", max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.name}'

class Address(models.Model):
    '''
    Model for storing addresses.
    '''
    TITLE_CHOICES = [
        ('Sir', 'Sir'),
        ('Madam', 'Madam'),
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="addresses")

    name = models.CharField(verbose_name="Address name", max_length=25, blank=True, null=True)
    title = models.CharField(verbose_name="Formal title", max_length=25, blank=True, null=True, choices=TITLE_CHOICES, default="Sir")
    first_name = models.CharField(verbose_name="First name", max_length=25, blank=True, null=True)
    middle_name = models.CharField(verbose_name="Middle name", max_length=25, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last name", max_length=25, blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=25, blank=True, null=True, choices=GENDER_CHOICES, default='Mr')
    birthday = models.DateField(verbose_name="Birthday", blank=True, null=True)
    address1 = models.CharField(verbose_name="Address 1", max_length=50, blank=True, null=True)
    address2 = models.CharField(verbose_name="Address 2", max_length=50, blank=True, null=True)
    address3 = models.CharField(verbose_name="Address 3", max_length=50, blank=True, null=True)
    city = models.CharField(verbose_name="City/Town", max_length=50, blank=True, null=True)
    county = models.CharField(verbose_name="County", max_length=50, blank=True, null=True)
    state = models.CharField(verbose_name="State", max_length=50, blank=True, null=True)
    zip = models.CharField(verbose_name="ZIP/Postal Code", max_length=5, blank=True, null=True)
    country = CountryField(verbose_name="Country", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    phone = models.CharField(verbose_name="Phone", max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.name}'

class PaymentCard(models.Model):
    '''
    Model for storing payment cards.
    '''

    TYPE_CHOICES = [
        ('Credit card', 'Credit card'),
        ('Debit card', 'Debit card'),
        ('Charge card', 'Charge card'),
        ('Pre-paid card', 'Pre-paid card'),
        ('Business travel card', 'Business travel card'),
        ('Purchasing card', 'Purchasing card'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="payment_cards")

    name = models.CharField(verbose_name="Payment Card Name", max_length=25, blank=True, null=True)
    name_on_card = models.CharField(verbose_name="Name on Card", max_length=50, blank=True, null=True)
    type = models.CharField(verbose_name="Type", max_length=30, blank=True, null=True, choices=TYPE_CHOICES, default='Credit card')
    number = models.CharField(verbose_name="Number", max_length=19, blank=True, null=True)
    security_code = models.CharField(verbose_name="Security Code", max_length=3, blank=True, null=True)
    start_date = models.DateField(verbose_name="Start Date", blank=True, null=True)
    expiration_date = models.DateField(verbose_name="Expiration Date", blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: **** **** **** {self.number[-4:]}'

class BankAccount(models.Model):
    '''
    Model for storing bank accounts.
    '''
    TYPE_CHOICES = [
        ('Checking account', 'Checking account'),
        ('Saving account', 'Saving account'),
        ('Money market account', 'Money market account'),
        ('Certificate of deposite (CD) account', 'Certificate of deposite (CD) account'),
    ]


    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bank_accounts")

    name = models.CharField(verbose_name="Bank Account Name", max_length=25, blank=True, null=True)
    bank_name = models.CharField(verbose_name="Bank Name", max_length=25, blank=True, null=True)
    account_type = models.CharField(verbose_name="Account Type", max_length=50, blank=True, null=True, choices=TYPE_CHOICES, default="Checking account")
    routing_name = models.CharField(verbose_name="Routing Name", max_length=25, blank=True, null=True)
    account_number = models.CharField(verbose_name="Account Number", max_length=25, blank=True, null=True)
    swift_code = models.CharField(verbose_name="Swift Code", max_length=25, blank=True, null=True)
    iban_number = models.CharField(verbose_name="Iban Number", max_length=25, blank=True, null=True)
    pin = models.CharField(verbose_name="Pin", max_length=25, blank=True, null=True)
    branch_address = models.CharField(verbose_name="Branch Address", max_length=25, blank=True, null=True)
    branch_phone = models.CharField(verbose_name="Branch Phone", max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.name}'