# coding: utf-8

from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
                name='Antonio Miquelini',
                slug='antonio-miquelini',
                url='http://antoniomiquelini.net',
                description='Passionate software developer!')
        self.speaker.save()
        
    def test_create(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)
        
    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Antonio Miquelini', unicode(self.speaker))
        
class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Antonio Miquelini',
            slug='antonio-miquelini', url='http://antoniomiquelini.net',
            description='Passionate software developer!')
            
    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                                         value='antoniomiquelini@net')
        self.assertEqual(1, contact.pk)
        
    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
                                         value='11-765698655')
        self.assertEqual(1, contact.pk)
    
    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                                         value='11-889098655')
        self.assertEqual(1, contact.pk)
        
    def test_kind(self):
        'Contact kind should be linited to E, P, or F.'
        contact = Contact(speaker=self.speaker, kind='A', value='email ou fone ou fax')
        self.assertRaises(ValidationError, contact.full_clean)
        
    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(speaker=self.speaker, kind='E',
                          value='antonio@miquelini.net')
        self.assertEqual(u'antonio@miquelini.net', unicode(contact))
         
