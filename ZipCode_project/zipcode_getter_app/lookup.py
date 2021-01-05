from ajax_select import register, LookupChannel

from .models import Address

@register('street_name')
class AddressLoookup(LookupChannel):

	model = Address

	def get_query(self,q,request):
		return self.model.objects.filter(street_name__icontains=q)
	def  format_item_display(self, item):
		return  u"<span class='street name'>%s</span>"  % item.street_name