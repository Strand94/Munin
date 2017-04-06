from django.test import TestCase
from .models import User

#Tests registration
class UserTestCase(TestCase):
    def setUp(self):
        #Sets up a user with first, middle and last name.
        User.objects.create_user(username='person_a', email='oyvindks@stud.ntnu.no', school=None, first_name='Øyvind',
                                 middle_name='Kanestrøm', last_name='Sæbø', image='')

        #Sets up a user with first and last name.
        User.objects.create_user(username='person_b', email='', school=None, first_name='Øyvind', middle_name='',
                                 last_name='Sæbø', image='')

        #Sets up a user with first and middle name.
        User.objects.create_user(username='person_c', email='', school=None, first_name='Øyvind', middle_name='Kanestrøm',
                                 last_name='', image='')

        # Sets up a user with middle and last name.
        User.objects.create_user(username='person_d', email='', school=None, first_name='', middle_name='Kanestrøm',
                                 last_name='Sæbø', image='')

        # Sets up a user with first name.
        User.objects.create_user(username='person_e', email='', school=None, first_name='Øyvind', middle_name='',
                                 last_name='', image='')

        # Sets up a user with middle name.
        User.objects.create_user(username='person_f', email='', school=None, first_name='', middle_name='Kanestrøm',
                                 last_name='', image='')

        # Sets up a user with last name.
        User.objects.create_user(username='person_g', email='', school=None, first_name='', middle_name='',
                                 last_name='Sæbø', image='')

        # Sets up a user with no name.
        User.objects.create_user(username='person_h', email='', school=None, first_name='', middle_name='',
                                 last_name='', image='')

        # Sets up a professor with no name.
        User.objects.create_user(username='person_i', role = 'P', email='', school=None, first_name='', middle_name='',
                                 last_name='', image='')

        # Sets up a non-professor with no name.
        User.objects.create_user(username='person_j', role='S', email='', school=None, first_name='', middle_name='',
                                 last_name='', image='')


    #Tests get_full_name of user with first, middle ans last name (contains 'æ', 'ø' and 'å').
    def test_person_a(self):
        person_a = User.objects.get(username = 'person_a')
        self.assertEqual(person_a.get_full_name(), 'Øyvind Kanestrøm Sæbø')

    #Tests get_full_name of user with first and last name.
    def test_person_b(self):
        person_b = User.objects.get(username = 'person_b')
        self.assertEqual(person_b.get_full_name(), 'Øyvind Sæbø')

    #Tests get_full_name of user with first and middle name.
    def test_person_c(self):
        person_c = User.objects.get(username='person_c')
        self.assertEqual(person_c.get_full_name(), 'Øyvind Kanestrøm')

    #Tests get_full_name of user with middle and last name.
    def test_person_d(self):
        person_d = User.objects.get(username='person_d')
        self.assertEqual(person_d.get_full_name(), 'Kanestrøm Sæbø')

    #Tests get_full_name of user with first name.
    def test_person_e(self):
        person_e = User.objects.get(username='person_e')
        self.assertEqual(person_e.get_full_name(), 'Øyvind')

    #Tests get_full_name of user with middle name.
    def test_person_f(self):
        person_f = User.objects.get(username='person_f')
        self.assertEqual(person_f.get_full_name(), 'Kanestrøm')

    #Tests get_full_name of user with last name.
    def test_person_g(self):
        person_g = User.objects.get(username='person_g')
        self.assertEqual(person_g.get_full_name(), 'Sæbø')

    #Tests get_full_name of user with no name.
    def test_person_h(self):
        person_h = User.objects.get(username='person_h')
        self.assertEqual(person_h.get_full_name(), 'person_h')

    #Tests if get_lecturers() returns true for a professor.
    def test_get_lecturer(self):
        person_i = User.objects.get(username ='person_i')
        self.assertEqual(person_i.get_lecturers(), True)

    #Tests if get_lecturers() returns false for a professor.
    def test_get_lecturer(self):
            person_j = User.objects.get(username='person_j')
            self.assertEqual(person_j.get_lecturers(), False)