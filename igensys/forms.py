from django.db.models import fields
from django.forms import ModelForm
from .models import *

class fItems(ModelForm):
    class Meta:
        model= Items
        fields = ['Product', 'QuaPrice', 'Sizes']
        
class fProfileInfo(ModelForm):
    class Meta:
        model= ProfileInfo
        fields = ['First_name', 'Last_name', 'Email', 'Address', 'Contact_number', 'Notes']
        
class fPayment(ModelForm):
    class Meta:
        model= Payment
        fields = ['TDate', 'DDate', 'Pay']

