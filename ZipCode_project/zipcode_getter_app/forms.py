

#from ajax_select.fields import AutoCompleteField
from django import forms
from .models import Address

class  AddressForm(forms.ModelForm):
	class Meta: 

		model = Address
		fields = ['street_name']
		
	name = forms.CharField(label='street_name',max_length=100)


class StreetName(forms.Form):

	address_name = forms.CharField(label = 'Address', max_length = 100)