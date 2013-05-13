﻿# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager

'''
class Speaker(object):
        pass
'''        
'''
class Speaker(object):
        name = 'Antonio Miquelini'
        url = 'http://antoniomiquelini.net'
        description = 'Passionate software developer!'
'''
        
class Speaker(models.Model):
        name = models.CharField(_('Nome'), max_length=255)
        slug = models.SlugField(_('Slug'))
        url = models.URLField(_('Url'))
        description = models.TextField(_(u'Descrição'), blank=True)
        
        def __unicode__(self):
            return self.name
''' Refatorado conforme página 104 aula 4
from eventex.core.managers import (EmailContactManager, PhoneContactManager,
                                  FaxContactManager)
class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
        )
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)
    
    objects = models.Manager()
    email = EmailContactManager()
    phones = PhoneContactManager()
    faxes = FaxContactManager()
'''

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
        )
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)
    
    objects = models.Manager()
    email = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')
    
    def __unicode__(self):
        return self.value
        
        
    
    


        
  