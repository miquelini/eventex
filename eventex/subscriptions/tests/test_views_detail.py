# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Antonio Miquelini', cpf='13345678901',
                                        email='antoniocarlos@gmail.com', phone='11-988776620')
        self.resp = self.client.get('/inscricao/%d/' % s.pk)
        
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
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)