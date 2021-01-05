

from ajax_select.fields import AutoCompleteField
from django import forms
from .models import Address


class  AddressForm(forms.ModelForm):
	class Meta: 

		model = Address
		fields = ['street_name']
		
	name = AutoCompleteField('street_name')

class StreetName(forms.Form):

	address_name = forms.CharField(label = 'Adress', max_length = 100)