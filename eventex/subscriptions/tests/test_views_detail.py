# coding: utf-8
'''
#3 Aqui usaremos o urlresolvers para identificar a rota
'''

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r          #1 adicioinado

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Antonio Miquelini', cpf='13345678901',
                                        email='antoniocarlos@gmail.com', phone='11-988776620')
#3        self.resp = self.client.get('/inscricao/%d/' % s.pk)
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))
        
    def test_get(self):
        'Get /inscricao/1/ should return status 200.'
        self.assertEqual(200, self.resp.status_code)
        print ' - Get /inscricao/1/ should return status 200.'
        
    def test_template(self):
        'Uses templates'
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')
        print ' - Uses templates'
    
    def test_context(self):
        'Context must have a subscription instance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)
        print ' - Context must have a subscription instance.'
    
    def test_html(self):
        'Context must have a subscription instance.'
        self.assertContains(self.resp, 'Antonio Miquelini')
        print ' - Context must have a subscription instance.'
        
class DetailNotFound(TestCase):
    def test_not_found(self):
#3        response = self.client.get('/inscricao/0/')
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)