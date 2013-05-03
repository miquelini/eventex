# coding: utf8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        
    def test_get(self):
        'Get /inscricao/ must return status code 200 - Deve retornar status code 200.'
        self.assertEqual(200, self.resp.status_code)
        print " Testou se a pagina existe  ........."

    def test_template(self):
        'Response should be a rendered template. - Resposta deve ser um modelo rederizado'
        self.assertTemplateUsed(self.resp,
                               'subscriptions/subscription_form.html')
        print " Testou a renderizacao   ........."
        
    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')
        print " Testou se existem campos, entradas, tipos e botoes no formulario  ........."
        
    def teste_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        print " Testou o token ??????????   ........."
    
# Verifica se e um formulario.
    def test_has_form(self):
        'Context must have the subscription form - Contexto deve ter o formulario de inscricao.'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        print " Testou se e um formulario ..........."
        
# Teste movido para test_forms.py        
#    def test_form_has_fields(self):
#        'Form must have 4 fields.'
#        form = self.resp.context['form']
#        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
#        print "Testou se possui 4 campos em test_views_subscribe ..........."
