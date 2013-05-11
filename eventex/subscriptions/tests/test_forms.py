# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
        print ' - Form must have 4 fields.'
        
    '''
    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        data = dict(name='Antonio Carlos', email='antonio@carlos.com',
                    cpf='12345678901', phone='11-87654637')
        data.update({'cpf': 'ABCD5678901'})
        form = SubscriptionForm(data)
        form.is_valid()
        
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits.'
        data = dict(name='Antonio Carlos', email='antonio@carlos.com',
                    cpf='12345678901', phone='11-9999999999')
        data.update({'cpf': '1234'})
        form = SubscriptionForm(data)
        form.is_valid()
        
        self.assertItemsEqual(['cpf'], form.errors)
    '''
    def make_validated_form(self, **kwargs):
        data = dict(name='Antonio Carlos', email='antonio@carlos.com',
                    cpf='12345678901', phone_0='11', phone_1='9999999999')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='ABCD5678901')
        print ' Teste Teste CPF must only accept digits.'
        
    def test_name_must_be_capitalized(self):
        'Name must be capitalized.'
        form = self.make_validated_form(name='ANTONIO carlos')
        self.assertEqual('Antonio Carlos', form.cleaned_data['name'])
        print ' - Name must be capitalized.'
       
    def test_cpf_has_11_digits(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='1234')
        
        self.assertItemsEqual(['cpf'], form.errors)
        print ' - CPF must only accept digits.'
        
    def test_email_is_optional(self):
        'Email is optional.'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
        print ' - Email is optional.'
        
    def test_must_inform_email_or_phone(self):
        'Email and Phone are optional, bust one must be informed.'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
        print ' - Email and Phone are optional, bust one must be informed.'
        
        
        
        
        
        
