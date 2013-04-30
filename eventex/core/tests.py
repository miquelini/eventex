# coding: utf-8
"""
Aqui estomos importando a classe de teste TesteCase que podem ter multiplos cenários de testes
Criaremos uma classe para nosso teste de Homepage
Criaremos um método test_get para testar a existência e seu hatml
"""

from django.test import TestCase

class HomepageTeste(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_get(self):
        'Get / must return status code 200 - Deve retornar status code 200.'
        self.assertEqual(200, self.resp.status_code)
    def test_template(self):
        'Homepage must use template index.html - Homepage usa o modelo index.html'
        self.assertTemplateUsed(self.resp, 'index.html')