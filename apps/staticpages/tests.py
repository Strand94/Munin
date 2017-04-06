from django.test import TestCase
from .models import School


class SchoolTestCase(TestCase):
    def setUp(self):
        ntnu = School(name='Norsk Teknisk Naturvitenskaplig Universitet', abbriviation='ntnu', image='', telephone='', address='', place='', webpage='')
        ntnu.save()

    def test_return_abbreviation(self):
        self.assertEqual(School.objects.get(name='Norsk Teknisk Naturvitenskaplig Universitet').__str__(), 'ntnu')