from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.shortcuts import resolve_url as r



class HomeViewTest(TestCase):

    def test_home_status_code(self):       
        self.response = self.client.get(r('core:home'))
        self.assertEqual(self.response.status_code, 200)

    def test_home_template_used(self):
        self.response = self.client.get(r('core:home'))
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertTemplateUsed(self.response, 'base.html')