
from django.contrib import admin
#from ajax_select.admin import AjaxSelectAdmin
from .forms import AddressForm
from .models import Address
# Register your models here.

#@admin.register(Address)

class AddressAdmin(admin.ModelAdmin):#AjaxSelectAdmin

	pass