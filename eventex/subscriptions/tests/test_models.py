# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
        name='Antonio Miquelini',
        cpf='12345678901',
        email='antoniocarlos@gmail.com',
        phone='11-988776620'
        ) 
        
    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)
        print ' - Subscription must have name, cpf, email, phone'
        
    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)
        print ' - Subscription must have automatic created_at'
        
    def test_unicode(self):
        self.assertEqual(u'Antonio Miquelini', unicode(self.obj))
        print " - Testa a instancia com unicode u "
        
class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Antonio Miquelini', cpf='12345678901',
                                    email='antoniocarlos@gmail.com', phone='11-988776620')
                                    
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Antonio Miquelini', cpf='12345678901',
                          email='antoniocarlos@hotmail.com', phone='11-988776620')
        self.assertRaises(IntegrityError, s.save)
        print " - CPF must be unique"
        
    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Antonio Miquelini', cpf='00000000011',
                          email='antoniocarlos@gmail.com', phone='11-988776620')
        self.assertRaises(IntegrityError, s.save)
        print " - Email must be unique"

        