# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Users

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        u=Users(first_name='111',last_name='222',password='123456',appellation='5555',email='imaxu@sina.com',id_no='130102198403261218',mobile_phone=13653319585)
        u.save()
        self.assertEqual((u.id>0),True)
				