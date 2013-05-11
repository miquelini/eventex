# coding: utf8
"""
Aqui usaremos o urlresolvers para identificar a rota
Todo metodo de teste deve comecar com test_ do contrario o teste nao sera executado
""" 

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r 


class SubscribeTest(TestCase):
    def setUp(self):
#        self.resp = self.client.get('/inscricao/')
        self.resp = self.client.get(r('subscriptions:subscribe'))
        
    def test_get(self):
        'Get /inscricao/ must return status code 200 '
        self.assertEqual(200, self.resp.status_code)
        print ' - Get /inscricao/ must return status code 200 '

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp,
                               'subscriptions/subscription_form.html')
        print ' - Response should be a rendered template.'
        
    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')
        print ' - Html must contain input controls.'
        
    def teste_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        print ' - Html must contain csrf token.'
    
    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        print ' - Context must have the subscription form'
        
# Teste movido para test_forms.py        
#    def test_form_has_fields(self):
#        'Form must have 4 fields.'
#        form = self.resp.context['form']
#        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
#        print "Testou se possui 4 campos em test_views_subscribe ..........."

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Antonio Miquelini', cpf='12345678901',
                    email='antoniocarlos@gmail.com', phone='11-988776620')
#        self.resp = self.client.post('/inscricao/', data)
        self.resp = self.client.post(r('subscriptions:subscribe'), data)
    
    def test_post(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)
        print ' - Valid POST should redirect to /inscricao/1/'
    
    def test_save(self):
        'Valid POST must be saved.'
        self.assertTrue(Subscription.objects.exists())
        print ' - Valid POST must be saved.'
        
class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Antonio Miquelini', cpf='000000000012',
                    email='antoniocarlos@gmail.com', phone='11-988776620')
#        self.resp = self.client.post('/inscricao/', data)
        self.resp = self.client.post(r('subscriptions:subscribe'), data)
        
    def test_post(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.resp.status_code)
        print ' - Invalid POST should not redirect.'
        
    def test_form_errors(self):
        'Form must contain errors.'
        self.assertTrue(self.resp.context['form'].errors)
        print ' - Form must contain errors.'

    def test_dont_save(self):
        'Do not save data.'
        self.assertFalse(Subscription.objects.exists())
        print ' - Do not save data.'

       
class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Check if non_field_errors ara show in template.'
        invalid_data = dict(name='Antonio Carlos', cpf='11111111111')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        
        self.assertContains(response, '<ul class="errorlist">')
        print ' - Check if non_field_errors ara show in template.'

        
    
