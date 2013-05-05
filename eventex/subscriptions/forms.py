# coding: utf-8
 
# Refatorado conforme pagina 186
#from django import forms
#from django.utils.translation import ugettext as _

#class SubscriptionForm(forms.Form):
#    name = forms.CharField(label=_('Nome'))
#    cpf = forms.CharField(label=_('CPF'), max_length=11)
#    email = forms.EmailField(label=_('Email'))
#    phone = forms.CharField(label=_('Telefone'))
    
from django import forms
from eventex.subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
  